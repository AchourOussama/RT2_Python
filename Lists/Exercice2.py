from random import randint, random


ls=[chr(randint(97,122)) for i in range(20)]
print(ls)
voyelle=['a','e','i','y','u','o']
# for i in range (20):
#     if (ls[i] in voyelle):
#         ls.remove(ls[i])
#      #the problem is that you are removing item from ls (so decreasing the length of ls) and the interation range is still fixed to the initial one

#solution 1: deal with items rather than indexes
for item in ls:
    if (item in voyelle):
        ls.remove(item)

print(ls)

#solution2: use while(); we garanty that the len(ls) is being in update each time we remove an item (so we will not get an index out of range error)
i=0
while(i<len(ls)):
    if ls[i] in voyelle:
        ls.remove(ls[i])
    i+=1
        

print(ls)