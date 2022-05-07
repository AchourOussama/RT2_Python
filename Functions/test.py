
# l=[0,1,2]
# ls=l.copy()

# # def type(data):
# #     t=type(data)
# #     match type(data):
# #         case int:
# #             print("integer")



# def changelist(x):
#     #this function work on primitive types and mutable types
#     x.append(1)
#     return x


# print(ls)
# print(changelist(ls))
# print(ls)
# print(l)
# isn't as :
# print(ls,changelist(ls),ls,sep="\n")

# don't forget the global property of a variable  

def min_max(l):
    return min(l),max(l)

min=min_max(l)
print(type(min)) #output : tuple
print(min)


