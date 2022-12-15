import torch
import pickle
import lzma

from typing import List, Iterable, Set, Tuple, Dict
from transformers import AutoTokenizer, BertForTokenClassification


class NERDataset(torch.utils.data.Dataset):
    """
    PyTorch Dataset for NER.
    """

    def __init__(
        self,
        token_seq: List[List[str]],
        token2idx: Dict[str, int],
    ):
        self.token2idx = token2idx
        self.token_seq = [self.process_tokens(tokens, token2idx) for tokens in token_seq]

    def __len__(self):
        return len(self.token_seq)

    def __getitem__(
        self,
        idx: int,
    ) -> torch.LongTensor:
        return torch.LongTensor(self.token_seq[idx])
    
    @staticmethod
    def process_tokens(
        tokens: List[str],
        token2idx: Dict[str, int],
        unk: str = "<UNK>",
    ) -> List[int]:
        """
        Transform list of tokens into list of tokens' indices.
        """
        result = [
            token2idx[token] if token in token2idx else token2idx[unk]
            for token in tokens
        ]
        return result


class NERCollator:
    """
    Collator that handles variable-size sentences.
    """

    def __init__(
        self,
        token_padding_value: int,
    ):
        self.token_padding_value = token_padding_value

    def __call__(
        self,
        batch,
    ):

        tokens = [torch.LongTensor(i) for i in batch]
        tokens = torch.nn.utils.rnn.pad_sequence(tokens, batch_first=True, padding_value=self.token_padding_value)

        return tokens
    

class Solution:
    def __init__(self):
        with open("state.xz", "rb") as state_f:
            with open("config.xz", "rb") as config_f:
                state_data = state_f.read()
                config_data = config_f.read()
                
                filters = [{"id":lzma.FILTER_LZMA2,"dict_size":268435456, "preset":9, "mf":lzma.MF_HC3, "depth":0, "lc":3}]
                state_data = lzma.decompress(state_data, format=lzma.FORMAT_RAW, filters=filters)
                config_data = lzma.decompress(config_data, format=lzma.FORMAT_RAW, filters=filters)
                
                state = pickle.loads(state_data)
                config = pickle.loads(config_data)
                self.model = BertForTokenClassification.from_pretrained(config=config, state_dict=state, pretrained_model_name_or_path=None)
        
        self.tokenizer = AutoTokenizer.from_pretrained("pretrained_tokenizer")
        with open('token2idx.pkl', 'rb') as f:
            self.token2idx = pickle.load(f)
        
        with open('idx2label.pkl', 'rb') as f:
            self.idx2label = pickle.load(f)

    def predict(self, texts: List[str]) -> Iterable[Set[Tuple[int, int, str]]]:
        spans = []
        tokens = []
        for text in texts:
            span = self.tokenizer(text, return_offsets_mapping=True, add_special_tokens=False, truncation=True)['offset_mapping']
            spans.append(span)
            tokens.append([text[i[0]:i[1]] for i in span])
        
        dataset = NERDataset(
            token_seq=tokens,
            token2idx=self.token2idx,
        )

        collator = NERCollator(
            token_padding_value=self.tokenizer.pad_token_id
        )
        
        dataloader = torch.utils.data.DataLoader(
            dataset,
            batch_size=1,
            shuffle=False,
            collate_fn=collator,
        )


        ans = []

        for i, data in enumerate(dataloader):
            outputs_idx = self.model(data)["logits"].argmax(dim=-1)[0]
            outputs_labels = [self.idx2label[j.item()] for j in outputs_idx]
                
            pred = 'NOT_ENTITY'
            length = [-1, -1]
            text_ans = set()
            for j in zip(outputs_labels, spans[i]):
                if j[0][0] == 'B':
                    if pred != 'NOT_ENTITY':
                        text_ans.add((*length, pred))
                    length = [j[1][0], j[1][1]]
                    pred = j[0][2:]
                elif j[0][0] == 'I':
                    length[1] = j[1][1]
                else:
                    if pred != 'NOT_ENTITY':
                        text_ans.add((*length, pred))
                    length = [-1, -1]
                    pred = 'NOT_ENTITY'
            else:
                if pred != 'NOT_ENTITY':
                    text_ans.add((*length, pred))
            
            ans.append(text_ans)
        return ans
