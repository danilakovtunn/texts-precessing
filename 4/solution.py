import pickle
import numpy as np

from sklearn import neighbors

class Solution:
    def __init__(self):
        with open('knn.pkl', 'rb') as f:
            self.model = pickle.load(f)
        with open('normalizer.pkl', 'rb') as f:
            self.scaler = pickle.load(f)
        with open('X.pkl', 'rb') as f:
            self.X = pickle.load(f).tolist()
        with open('y.pkl', 'rb') as f:
            self.y = pickle.load(f).tolist()
        self.cnt = 0
            
    def predict(self, text: str) -> str:
        data = self.scaler.transform(np.array([text]))
        ans = self.model.predict(data)[0]

        self.X.append(text)
        self.y.append(ans)
        self.cnt += 1
        if self.cnt % 50 == 0:
            X_tf = self.scaler.transform(np.array(self.X))
            self.model = neighbors.KNeighborsClassifier(metric='cosine', n_neighbors=1, weights='distance')
            self.model.fit(X_tf, self.y)

        return str(ans)

