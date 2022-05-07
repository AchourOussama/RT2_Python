from numbers import Number
class exerciceException (Exception):
    pass

def average(n):
    i=0
    sum=0
    while(i<n):
        valid = False
        while not valid:
            mark=float(input("mark {}:".format(i+1)))
            if mark < 0 or mark > 20 or (not isinstance(mark,float)):
                raise exerciceException
            else :
                valid=True
                sum+=mark

        i+=1
    print("average: {:.2f}".format(sum/n))

try:
    average(5)
except exerciceException as e:
    print("mark is not valid, it should be a float included in [0-20]")

except Exception as e:
    print("external error")
