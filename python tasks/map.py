list1=[1,2,3,4,5]
mlist=map(lambda a:a+10,list1)
print(list(mlist))


list1=[1,2,3,4,5]
mlist=list(map(lambda a:a+10,list1))
print(mlist)


print("\n")
#filter
list1=[1,2,3,4,5]
flist=filter(lambda a:a%2==0,list1)
print(list(flist))

print("\n")
#reduce
from functools import reduce
list1=[1,2,3,4,5]
rlist=reduce(lambda a,b:a+b,list1)  
print(rlist)


list1=[1,2,3,4,5,6,7,8]
mlist=map(lambda a:a+10,list1)
flist=filter(lambda a:a%2==0,list1)
rlist=reduce(lambda a,b:a+b,list1)
print(rlist)
print(list(mlist))
print(list(flist))



list1=[1,2,3,4,5]
mlist=map(lambda a:a%2==0,list1)
print(list(mlist))


print("\n")

def sum(a):
    if a==1:
        return 1
    elif a==0:
        return 0
    else:
        return a+sum(a-1)
print(sum(0))


print("\n")

def sum(a):
    if a==1:
        return 1
    elif a==0:
        return 0
    else:
        return a*sum(a-1)
print(sum(5)) 











