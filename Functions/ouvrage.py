def ouvrage(*args,**supp):
    for i in args:
         print(i,end=" ")
    print()
    for i in supp:
        print("{} : {}".format(i,supp[i]))

ouvrage("Atomic Habits",Author_name="idk",pages=400,release_date="1/1/2019")
