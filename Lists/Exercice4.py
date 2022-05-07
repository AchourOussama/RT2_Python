l = [[1,2,3], [4,5,6], [7,8,9]]
list=[l[i][j] for i in range(len(l)) for j in range(len(l[i]))]
print(list)