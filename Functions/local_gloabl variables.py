from glob import glob


def change():
    global x
    x+=1
    return(x)

x= 5
print(x)
print(change())
print(x)
