import re


def SubString(str,sub):
    #string.find(subString,start,end)
    #ls of indexes:
    index=[]
    i=str.find(sub)
    while(i != -1):
        index.append(i)
        i=str.find(sub,i+len(sub))

    print("number of substrings : {0}".format(str.count(sub)))
    return index
    
ls=SubString("heheehe","he")
print(ls)   
