import string

class NameException (Exception):
    def __init__(self,message:string) :
        self.message=message
    
        
    

def Greeting(name):
    if (name==""):
        raise NameException("name should not be empty !")
    elif((not isinstance(name,str)) or (not name.isalpha()) ):
        
        raise NameException("please enter a valid name !")
     
    else :
        print("Good Morning "+name)

try:
    Greeting("")
except NameException as e:
    print(e.message)