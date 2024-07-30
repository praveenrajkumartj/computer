#day11 tasks
#task 1 to task 11
#total-16

#1.fact0rial

num=int(input("enter the number"))
factorial=1

for i in range(1,num + 1):    
       factorial = factorial*i    
print("The factorial of",num,"is",factorial)




#2.reverse the number

n=int(input("enter the number"))

rev=0


while n>0:
    s=n%10
    rev=rev*10+s
    n //=10
print(rev)





#4.sum the  digits number

n=int(input("enter the number"))     

d=0

while n>0:
    s=n%10
    d=d+s
    n//=10
print(d)





#10.pyramid
n=int(input())
for i in range(1,n+1):
    print(" "*(2*(n-i)),end="")
    
    for j in range(1,2*i):
        print("* ",end="")
    print()




#11.inverse pyramid
n=int(input())
for i in range(n,0,-1):
    print(" "*(2*(n-i)),end="")
    
    for j in range(1,2*i):
        print("* ",end="")
    print()






#6.COUNT HOW MANY VOWELS AND CONSTANT IN A STRING
word=input("enter the word:").lower()
vowel=0
constant=0



for i in word:
    if i in "aeiou":
           vowel=vowel+1
    else:
        constant=constant+1
print("vowels:",vowel)
print("costant:",constant)





#8.patternusing nested for loop
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()





#3.palindrome
num=int(input("enter the number"))
print(num)
r=0
t=num
while(num>0):
    d=num%10
    r=r*10+d
    num//=10
if t==r:
    print(r,"it is palindromenumber")
else:
    print(r,"it is not palindrome number")


    



#9.task
n=int(input())
for i in range(1,n+1):
    print(" "*(n-i),end="")
    
    for j in range(1,i+1):
        print("* ",end="")
    print()





#5.divide
num=int(input("enter thr number"))
if num%2==0 and num%3==0:
    print("it is divisible by 2 and 3")
elif num%2==0 and num%3!=0:
       print("it is divible by 2 and not by 3")
elif num%3==0 and num%2!=0:
       print("it is divible by 3 and not by 2")
else:
    print("it is not divisible by 2 and 3")





#7.task7    
string=input("enter a string:")
o=input("enter the subs to replace:")
n=input("enter the new subs :")
print("modifiedstring:",string.replace(o,n))


    





    
    




