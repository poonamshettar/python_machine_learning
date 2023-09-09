list=[]
list1=[]
list2=[]
for i in range(10):
    x=int(input())
    list.append(x)
for x in list:
    if(x%2==0):
        list1.append(x)#for even numbers
    else:
        list2.append(x)#for odd numbers
    
print(list1)
print(list2)