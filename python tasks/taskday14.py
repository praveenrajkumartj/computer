print("day 14 task 1 to 7")
print("OUTPUT\n")
#task:1
print("Task:1")
list1=["edex",1,4,5]
list2=["Tech",3,4,5]
print(list1)
print(list1[0])
print(list1[2:4])
print(list1[1:4])
list2=list2+list2
print(list2)
list2=["Tech",3,4,5]
list1=list1+list2  
print(list1)
print("\n")

#task:2

print("Task:2")
list1=[10, 20, 30, 'New Delhi', 'Mumbai']
print("list elements are:",list1)
list2=[40,50,"chennai"]
list1.extend(list2)
print("list elements are:",list1)
list1.pop()
print("list elements are:",list1)
list1.pop(6)
print("list elements are:",list1)
print("\n")

#task:3
print("Task:3")
list1=[10, 20, 30, 40, 50]
sum=0
print("list elements are:")

for i in list1:
    print(i)
    sum+=i
print("sum is:",sum)
print("\n")

#task:4
print("Task:4")
list1=[10, 20, 30, 40, 30]
print("original list:",list1)
list1.remove(30)
print("list after removing 30:",list1)
list1.remove(10)
print("list after removing 10:",list1)
print("\n")

#task:5
print("Task:5")
num=int(input("enter the value:"))
list1=[10, 20, 10, 30, 10, 40, 10, 50]
print("original list:\n",list1)
for i in list1:
    if i==num:
        list1.remove(num)
print("list after removing elements:\n",list1)
print("\n")


#task:6
print("Task:6")    
list1=[10, 20, 30, 40, 50]
print("original list:",list1)
list1.pop(1)
list1.pop(1)
print("updated list after deleting the element:\n",list1)
print("\n")


#task:6
print("Task:6")
list1=[10, 20, 30, 40, 50]
print("original list:",list1)
del list1[1:3]
print("updated list after deleting the element:\n",list1)
print("\n")

#task:7
print("Task:7")
list1=[10, 20, 10, 20, 30, 40, 50]
print(list1)
element=int(input("enter the element in the list which index value do you want to know: "))

print("index of first matched",element,"is:",list1.index(element))
print("\n")


#task 8
print("Task:8")
n=int(input("enter the limit:"))
list1=[]
for i in range(1,n+1):
    h=int(input("enter the value"))
    list1.append(h)
print("input list elements are:",list1)
print("\n")


#task: 10
print("Task:10")
list1=[11,22,33,44,55]
print("list=",list1)
list2=[]
list3=[]
for i in list1:
    if i%2==0:
        n=i
        list2.append(n)
    elif i%2!=0:
        n=i
        list3.append(n)
print("list with Even numbers:",list2)
print("list with Odd numbers:",list3)
print("\n")


#task 11
print("Task:11")
list1=[10,15,20,25,30]
print("list=",list1)
m=int(input("M="))
n=int(input("N="))
for i in list1:
    if i%m==0 and i%n==0:
        print(i,end=" ")
print("\n")


#task: 11
print("Task:11")
list1=[10,15,20,25,30]
print("list=",list1)
list2=[]
m=int(input("M="))
n=int(input("N="))
for i in list1:
    if i%m==0 and i%n==0:
        h=i
        list2.append(h)
print(list2)
print("\n")



#task:12
print("Task:12")
s=int(input("enter the start value="))

e=int(input("enter the end value="))

list1=[]
list2=[]
list3=[]
j=3
for i in range(s,e+1):
    n=i
    h=i*i
    g=i**j
    list1.append(n)
    list2.append(h)
    list3.append(g)
print("numbers:",list1)
print("squares:",list2)
print("cubes:",list3)
print("\n")


#task:15
print("Task:15")

list1=[11,22,33,44,55]
print("original list:\n",list1)
for i in list1:
    if i%2==0:
        list1.remove(i)
print("list after removing even elements:\n",list1)
print("\n")


#task:18
print("Task:18")
list1=[4,-1,5,9,-6,2,-9,8]
list2=[]
list3=[]
for i in list1:
    if i>0:
        n=i
        list2.append(n)
    else:
        h=i
        list3.append(h)
print("even number in list:",list2)
print("odd number in list:",list3)
print("\n")



#task:19
print("Task:19")
list1=[4, 1, 6, 3, 9]
mul=1
print("list=",list1)
for i in list1:
    mul=mul*i
print("multiplication of list value:",mul)
print("\n")



#task:20
print("Task:20")
list1=[3, 6, 9, 8, 1]
print("list=",list1)
l=0
for i in list1:
    l=l+1
print("length of the list",l)    
print("\n")


#task:21
print("Task:21")
list1=[4, 2, 9, 5, 1, 0, 7]
print("list=",list1)
n = int(input("Enter the value "))

if n in list1:
    print("present")
else :
    print("not found")
print("\n")    


#task:09
print("Task:09")    
list1=[10,20,30,40,50,10,20,30,40,50]
list2=[]
for i in list1:
    if i not in list2:
        list2.append(i)
print(list2)
print("\n")

#task:22
print("Task:22")
list1= [[2, 3, 4], [3, 2, 4], [5, 8]]
print("assume input is:",list1)
list2=[]
for i in list1:
    for j in i:
        list2.append(j)
print("Output is :",list2)        
                    
        








    



    



    
    





