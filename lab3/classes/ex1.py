class asda:
    def __init__(self):
        self.input=""
    def getString(self):
        self.input= input()
    def printString(self):
        print(self.input.upper())

asd=asda()
asd.getString()
asd.printString()