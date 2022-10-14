import unittest
import re

class Tests(unittest.TestCase):
    def testNUM1(self):
        v = f"^({NUM_256})$"
        for i in range(256):
            self.assertRegex(str(i), v)

    def testNUM2(self):
        v = f"^({NUM_100})$"
        for i in range(101):
            self.assertRegex(str(i), v)

    def testNUM3(self):
        v = f"^({NUM_360})$"
        for i in range(361):
            self.assertRegex(str(i), v)

    def testColor(self):
        v = fr"^({COLOR_REGEXP})$"
        self.assertRegex("#21f48D", v)
        self.assertRegex("#888", v)
        self.assertRegex("rgb(255, 255,255)", v)
        self.assertRegex("rgb(10%, 20%, 0%)", v)
        self.assertRegex("hsl(200,100%,50%)", v)
        self.assertRegex("hsl(0, 0%, 0%)", v)
        
        
        self.assertNotRegex("#2345", v)
        self.assertNotRegex("ffffff", v)
        self.assertNotRegex("rgb(257, 50, 10)", v)
        self.assertNotRegex("rgb(0, 50, 130%)", v)
        self.assertNotRegex("hsl(20, 10, 0.5)", v)
        self.assertNotRegex("hsl(34%, 20%, 50%)", v)


    def testPassword(self):
        v = fr'^({PASSWORD_REGEXP})$'
        self.assertRegex("rtG3FG!Tr^e", v)
        self.assertRegex("aA1!*!1Aa", v)
        self.assertRegex("oF^a1D@y5e6", v)
        self.assertRegex("enroi#$rkdeR#$092uwedchf34tguv394h", v)
        self.assertRegex("pAs$w0rd!", v)     
        self.assertRegex("aA1!*&^$&^#@%&^$!@*#&^*&%$&!@^#*&!@*#!@*&@*$^*&!@", v)

        self.assertNotRegex("пароль", v)
        self.assertNotRegex("pA$$w0rd", v)
        self.assertNotRegex("password", v)
        self.assertNotRegex("qwerty", v)
        self.assertNotRegex("lOngPa$$W0Rd", v)        
        self.assertNotRegex("pAs$w0rd", v)     
        self.assertNotRegex("pAs^w0rd", v) 
        self.assertNotRegex("pAs*w0rd", v)

    def testDate(self):
        v = fr'^({DATES_REGEXP})$'
        self.assertRegex("20 января 1806", v)
        self.assertRegex("1924, July 25", v)
        self.assertRegex("1635/09/26", v)
        self.assertRegex("1111.09.26", v)
        self.assertRegex("1000-09-26", v)
        self.assertRegex("26/09/1635", v)
        self.assertRegex("3.1.1506", v)
        self.assertRegex("Jan 12, 2006", v)
        self.assertRegex("February 28, 2007", v)
        
        self.assertNotRegex("February 29, 2001", v)
        self.assertNotRegex("Jan 33, 2121", v)
        self.assertNotRegex("25.08-1002", v)
        self.assertNotRegex("декабря 19, 1838", v)
        self.assertNotRegex("8.20.1973", v)
        self.assertNotRegex("Jun 7, -1563", v) 
        

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
VARIABLE = r'(?P<variable>\b[a-zA-Z_]\w*\b)'
NUMBER = r'(?P<number>\b\d+[\.]?\d*\b)'
CONSTANT = fr'(?P<constant>\b({CONSTS})\b)'
FUNCTION = fr'(?P<function>\b({FUNCS})\b)'
OPERATOR = r'(?P<operator>\^|\*|\/|\-|\+)'
LEFT_PAR = r'(?P<left_parenthesis>\()'
RIGHT_PAR = r'(?P<right_parenthesis>\))'
EXPRESSION_REGEXP = fr'{FUNCTION}|{CONSTANT}|{NUMBER}|{OPERATOR}|{LEFT_PAR}|{RIGHT_PAR}|{VARIABLE}'

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

if __name__ == "__main__":
    # тесты
    regexp = re.compile(EXPRESSION_REGEXP)
    for match in regexp.finditer("sin(x) + cos(y) * 2.5"):     
        print(f'type: {match.lastgroup}, span: {match.span()}')
    print()

    for match in regexp.finditer("pi    +        usO5NlMvU"):     
        print(f'type: {match.lastgroup}, span: {match.span()}')
    print()

    for match in regexp.finditer("(         63393394.98 /8505      )"):     
        print(f'type: {match.lastgroup}, span: {match.span()}')
    print()

    for match in regexp.finditer("(         2*pie + sqrt23  + pi    )"):     
        print(f'type: {match.lastgroup}, span: {match.span()}')
    print()

    for match in regexp.finditer("(         exp    ln1   )"):     
        print(f'type: {match.lastgroup}, span: {match.span()}')
    print()
    unittest.main()

