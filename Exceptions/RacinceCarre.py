import math
valid=False
while not valid:
    n=int(input("number: "))
    try:
        print("number{0}\nSquare root of {0}: {1}".format(n,math.sqrt(n)))
        valid=True
    except Exception as e:
        print("no square root operation for negative number")

   