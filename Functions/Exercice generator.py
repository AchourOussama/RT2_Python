tuple=(i for i in range(100))

def generator(t):
    for i in t:
        yield i**2

gen=generator(tuple)

for i in gen:
    print(i)

