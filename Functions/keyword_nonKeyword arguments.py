# from unicodedata import name


# def show(*args):
#     #args is a tuple
#     for i in args:
#         print(i,end=" ")

# def show1(**Kwargs):
#     print(type(Kwargs))
#     for i in Kwargs:
#         print("{} : {}".format(i,Kwargs[i]))

# show1(name="Achour",age=20,date_of_birth="10/12/2001")

#mixing *agrs and **kwargs

def data(*args,**kwargs):
    for i in args:
         print(i,end=" ")
    print()
    for i in kwargs:
        print("{} : {}".format(i,kwargs[i]))
    
    
data(1,2,3,name="Achour",age=20,date_of_birth="10/12/2001")
#data(1,2,name="Achour",3,age=20,date_of_birth="10/12/2001")#error:positional argument cannot appear after keyword argument 
    
