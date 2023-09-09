x=int(input("Enter number"))
for i in range(2,x+1):
    if(x%i==0):
        break
if(x==i):
    print("prime")
elif(x%3==0):
    print("divisible by 3")
elif(x%5==0):
    print("divisible by 5")
elif(x%7==0):
    print("divisible by 7")
elif(x%11==0):
    print("divisible by 11")
else :print("not prime and not divisible")