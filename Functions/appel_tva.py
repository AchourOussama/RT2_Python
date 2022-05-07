import tva 
#print(type(tva)) --> module
#print(tva.__name__) --> tva

sum=float(input("sum of money: "))
print("sum of money after taxes: ",tva.pttc_reduit(sum))
 