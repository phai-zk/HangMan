import random

class GameRule:
    WORD='''Unusual
Strange
Odd
Peculiar
Abnormal
Unique
Rare
Bizarre
Exceptional
Eccentric
Outlandish
Curious
Quirky
Atypical
Out of the ordinary
Uncommon
Offbeat
Singular
Anomalous
Weird'''

    def __init__(self):
        self.chios = ("A B C D E F G H I J K L M N O P Q R S T U V W X Y Z").split(" ")
        self.generate()

    def generate(self):
        word = GameRule.WORD.split("\n")
        idx = random.randint(0,len(word))
        self.word = word[idx]
        self.setAnswer()
        return (word[idx])

    def setAnswer(self):
        self.answer = []
        for i in range(len(self.word)):
            if(self.word[i] == " ") :
                self.answer.append(" ")
            else :
                self.answer.append("_")

    def check(self, ans = ""):
        found = False
        for i in range(len(self.word)):
            if (ans.upper() == self.word[i].upper()):
                if (i > 0):
                    self.answer[i] = ans.lower()
                else:
                    self.answer[i] = ans.upper()
                found = True
        
        idx = self.chios.index(ans.upper())
        self.chios[idx] = "_"
        return (found)
    
    def endGame(self):
        if (("").join(self.answer) == self.word):
            return True
        return False