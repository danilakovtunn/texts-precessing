# 1 упражнение
PASSWORD_REGEXP = r'(?!.*(?P<b2>[$^%@#&*!?\da-zA-Z])(?P=b2).*)(?=(.*(?P<b1>[%$^%@#&*!?]).*(?!(?P=b1))(?=[%$^%@#&*!?]).*[%$^%@#&*!?]))(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?:[$^%@#&*!?\da-zA-Z]){8,}'

# 2 упражнение
NUM_100 = r'((?:[1-9])?[0-9]|100)'
NUM_256 = r'((?:[1-9])?[0-9]|1(?:[0-9]){2}|2[0-4][0-9]|25[0-5])'
NUM_360 = r'([0-9]|[1-9][0-9]|[1-2][0-9][0-9]|3[0-5][0-9]|360)'
RGB = fr'(rgb\(({NUM_256}|{NUM_100}%), *({NUM_256}|{NUM_100}%), *({NUM_256}|{NUM_100}%)\))'
HEX = r'#((?:[0-9a-fA-F]){6}|(?:[0-9a-fA-F]){3})'
HSL = fr'(hsl\({NUM_360}, *{NUM_100}%, *{NUM_100}%\))'
COLOR_REGEXP = fr'{RGB}|{HEX}|{HSL}'

# 3 упражнение
CONSTS = r'pi|e|sqrt2|ln2|ln10'
FUNCS = r'sin|cos|tg|ctg|tan|cot|sinh|cosh|th|cth|tanh|coth|ln|lg|log|exp|sqrt|cbrt|abs|sign'
VARIABLE = fr'(?P<variable>(?!({CONSTS}|{FUNCS})(?![a-zA-Z_0-9]))[a-z_](?:[a-zA-Z_0-9])*)'
NUMBER = r'(?P<number>(0|[1-9](?:[0-9])*)(?:\.(?:[0-9])*[1-9])?)'
CONSTANT = fr'(?P<constant>{CONSTS})'
FUNCTION = fr'(?P<function>{FUNCS})'
OPERATOR = r'(?P<operator>\^|\*|/|-|\+)'
LEFT_PAR = r'(?P<left_parenthesis>\()'
RIGHT_PAR = r'(?P<right_parenthesis>\))'
EXPRESSION_REGEXP = fr'{VARIABLE}|{NUMBER}|{CONSTANT}|{FUNCTION}|{OPERATOR}|{LEFT_PAR}|{RIGHT_PAR}'

# 4 упражнение
NUM_28 = r'(0?[1-9]|1[0-9]|2[0-8])'
NUM_30 = r'(0?[1-9]|[1-2][0-9]|30)'
NUM_31 = fr'({NUM_30}|31)'
NUM_12_31 = r'(0?[13578]|1[02])' #1,3,5,7,8,10,12
NUM_12_30 = r'(0?[469]|11)' #4,6,9,11
NUM_12_28 = r'(0?2)'
YEAR = r'([1-9]\d*|0)'
MONTH_RUS_28 = r'(февраля)'
MONTH_RUS_31 = r'(января|марта|мая|июля|августа|октября|ноября|декабря)'
MONTH_RUS_30 = r'(апреля|июня|сентября|ноября)'
MONTH_ENG_28 = r'(February|Feb)'
MONTH_ENG_31 = r'(January|Jan|March|Mar|May|July|Jul|August|Aug|October|Oct|December|Dec)'
MONTH_ENG_30 = r'(April|Apr|June|Jun|September|Sep|November|Nov)'
DDMMYYYY = fr'{NUM_28}((?P<del1>[/.-]){NUM_12_28}(?P=del1)| {MONTH_RUS_28} ){YEAR}|{NUM_30}((?P<del2>[/.-]){NUM_12_30}(?P=del2)| {MONTH_RUS_30} ){YEAR}|{NUM_31}((?P<del3>[/.-]){NUM_12_31}(?P=del3)| {MONTH_RUS_31} ){YEAR}'
YYYYMMDD = fr'{YEAR}((?P<sep1>[/.-]){NUM_12_28}(?P=sep1)|, {MONTH_ENG_28} ){NUM_28}|{YEAR}((?P<sep2>[/.-]){NUM_12_30}(?P=sep2)|, {MONTH_ENG_30} ){NUM_30}|{YEAR}((?P<sep3>[/.-]){NUM_12_31}(?P=sep3)|, {MONTH_ENG_31} ){NUM_31}'
MMDDYYYY = fr'{MONTH_ENG_28} {NUM_28}, {YEAR}|{MONTH_ENG_30} {NUM_30}, {YEAR}|{MONTH_ENG_31} {NUM_31}, {YEAR}'
DATES_REGEXP = fr'{DDMMYYYY}|{YYYYMMDD}|{MMDDYYYY}'
