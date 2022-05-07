
months=["Januray","February","March","April","May","June","July","August","September","October","November","December"]
days=[31,28,31,30,31,30,31,31,30,31,30,31]

#we suppose  list1 and list2 have the same length:
def couple(l1,l2):
    ls=[]
    for (i,j) in zip(l1,l2):
        ls.append((i,j))
    return ls
#method2:
def couple(l1,l2):
    ls=[]
    for i in range(len(l1)):
        ls.append((l1[i],l2[i]))
    return ls
couples=couple(months,days)
print(couples)
    
