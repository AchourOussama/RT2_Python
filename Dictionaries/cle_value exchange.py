def exchange(dic):
    #classic solution
    # d={}
    # for key,value in dic.items():
    #     d[value]=key
    # return d
    #comprehension:
    return {value:key for key,value in dic.items()}    

AnFr={"good":"bien","perfect":"parfait","drink":"boire"}
FrAn=exchange(AnFr)
print("English French dictionnary:\n{}\nFrench English dictionnary:\n{}".format(AnFr,FrAn))
