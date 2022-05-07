l=[1,4,2,4,0,3,1,1,8,7,2]

#expected output: ls=[0,1,2,3,4,7,8] (eleminating occurances and sorting the final list)
def occ_sort(l):
    #the idea to check each time whether the value in l already exists in the new list or not  
    ls=[]
    for i in range(len(l)):
        if (l[i] in ls ) == False:
            ls.append(l[i])
               
    ls.sort()
    return ls
print(l)
print(occ_sort(l))


    