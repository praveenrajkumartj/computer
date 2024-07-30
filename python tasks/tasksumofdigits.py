#sum of digits using recursion in different methods
def sum(a):
    if a==1:
        return 1
    elif a==0:
        return 0
    else:
        return a%10+sum(a//10)
print(sum(9345))


print("\n")




n=int(input("enter the number :"))
def sum(a):
    if a==1:
        return 1
    elif a==0:
        return 0
    else:
        return a%10+sum(a//10)
print(sum(n))



print("\n")


n=int(input("enter the number :"))
def sum(a):
    if a<=9:
        return a
   
    else:
        return a%10+sum(a//10)
print(sum(n))

