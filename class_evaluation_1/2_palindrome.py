y=input("Enter string ")
x=len(y)
for i in range(x):
    if(y[i]!=y[x-i-1]):
        break
if(i==x-1):
    print("palindrome")
else :
    print("not palindrome")