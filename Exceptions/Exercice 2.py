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
    
    
#More Detailed Proposed Solution    

class EmptyStringException(Exception):
    pass

class AlphaOnlyString(Exception):
    pass

def say_hello(name):
    if(name==""):
        raise EmptyStringException
    if(name.isalpha()==False):
        raise AlphaOnlyString
    print("Hello {0}".format(name))

try:
    say_hello("")
except EmptyStringException as e:
    print("string shouldn't be empty")
except AlphaOnlyString as a:
    print("should only contains alphabets")
