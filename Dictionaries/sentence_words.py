
#classic solution :
def words(stc):
    ls=stc.split(" ")
    wordsSet=set(ls)
    d={w:ls.count(w) for w in wordsSet}
    return d


stc=input("sentence :\n")
for key,value in words(stc).items():
    print(key,"\t",value)

#creating a class Sentence:

class Sentance :
    def __init__(self,str):
        self.value=str
        self.__words__=self.__words__()

    def __words__ (self):
        ls=self.value.split(" ")
        wordsSet=set(ls)
        d={w:ls.count(w) for w in wordsSet}
        return d

    def showWords(self):
        for key,value in self.__words__.items():
            print(key,"\t",value)


stc=Sentance("hello oussama . oussama is a smart guy . he is a unique man . A man of principales . A man of quality ." )
stc.showWords()