#matrice n*m
l = [[1,2,3], [4,5,6]]
#expected output: list=[[1, 4], [2, 5], [3, 6]]

#method1: function
def transposer(list):
    ls=[]
    for i in range(len(list[0])):
        row=[]
        for j in range(len(list)):
            row.append(list[j][i])
        ls.append(row)
    return ls

print(transposer(l))

#method2: list comprehension
#i index : row , j index : column
ls=[ [l[j][i] for j in range(len(l))] for i in range(len(l[0]))]
print(ls)


