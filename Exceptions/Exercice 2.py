from tokenize import String


def say_Moring(name):
    if (name=="")or(not isinstance(name,str)):
        raise Exception 
    else :
        print("Good Moring "+name)

try:
    say_Moring(name)
except Exception as e:
    print("name should be string")