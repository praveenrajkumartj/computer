#Funtions...

#key points..

#1) Reusability

# 2) Modularity 

#3) Abstraction


#funtions:

#1)create , call
#2)retrun , arguments





'''

def display():
    print("Hello")
display()

#OP - Hello

'''
'''
def display():
    print("Hello")

def display2():
    return "world"
display()   
print(display2())

#op
Hello
world
'''
#Have to use print statement while using return key ...
  #Arguments should be passed in funtions...ex(10,5)

'''
def display():
    a=10
    b=6
    print(a+b)
                      
display()

def display2(a,b):
    print(a+b)

display2(10,5)



def display(a,b):
    return a+b

print(display(10,6))
'''
'''
def display(a,b):
    
    
    return a+b
print(display(10,6))
'''   

#op - 16



#No return with Arguments...

'''
def add(a,b):
    print(a+b)
add(10,6)
'''


#No return without Arguments
'''

def add1():
    print("Funtions")
add1()
''' 

#return with arguments
'''
def add3(a,b):
    return a*b
print(add3(10,5))

'''
#Return without Arguments
'''
def add4():
    return "funtions"

print(add4())

'''


#Arguments type

#  1 )Arbitary Arguments ---*
'''
def stu(*a):
    print(a)

stu("vijay")
stu("ajith","madurai")
stu("vijay","madurai","MBA")

#op - when we use * op will be like tuple
"" 
('vijay',)
('ajith', 'madurai')
('vijay', 'madurai', 'MBA')
'''

'''
def add(*number):
    sum=0
    for i in number:
        sum=sum+i

    print(sum)



add(5)
add(5,6)
add(7,7)
'''



# 2)Keyword arguments

'''

def stu(name,location,course):


    print("name",name)
    print("location",location)
    print("course",course)

stu(location="madurai",name="vijay",course="python")

'''


# 3)Arbitary keyword Argumets ----** values & keyword should be added...
'''
def employe(**data):
    print(data)

employe(name="vijay",age=50,loc="madurai")
employe(name="ajith",age=51)
'''
#op - output will be like dictiorany...

'''
{'name': 'vijay', 'age': 50, 'loc': 'madurai'}
{'name': 'ajith', 'age': 51}
'''

#4) Default arguments...(Default parameters) (Coimbatore is the default value)


'''
def stu(name,loc="coimbatore",course="python"):
    print(name,loc,course)

stu("vijay","Madurai")
stu("Ajith")
'''
#op
'''
vijay Madurai python
Ajith coimbatore python
'''

#important
'''
def dis(a,b,c=0):
    print(a,b,c)

dis(5,6)
'''
#op
'''
5,6,0
'''

#Passing a list: ( list can be passed in this arguments)
'''

def display(a):
    print(a)

display(5)

display([1,2,3,4,5])

#op

5
[1, 2, 3, 4, 5]

'''


#LAMBDA (Key word) (its a return funtion) (One liner)

#lambda funtion is ANONYMOUS (Peyar illatha ondru)

#map
#filter
#reduce
'''
lambda a,b : a+b
'''
#syntax

# lambda arguments : expression  
'''
name=lambda a,b : a+b

print(name(5,7))

#op - 10
'''


'''
name=lambda a : a**2

print(name(2))
print(name(4))
print(name(5))
'''

#op
'''
4
16
25

'''

#List comprehension....

#syntax

#[expression iteration funtion]


#[ i for i in range if==]

list2=[i for i in range(1,11)]

print(list2)
  
#op - [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''
list3=[i**2 for i in range(1,11)]

print(list3)
'''
#op - [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

'''

list4=[i for i in range(1,11) if i%2==0]

print(list4)

'''
#op - [2, 4, 6, 8, 10]



#lambda

#map (funt,iterable)

#filter (funt,iterable)

#reduce (funt,iterable)



# 1)map  - need to type cast (list)


list1= [1,2,3,4,5]

mlist=map(lambda a : a+10 , list1)

print(list+(mlist))

#or
'''
list1= [1,2,3,4,5]

mlist=list(map(lambda a : a+10 , list1))

print(mlist)
'''
#or
list1= [1,2,3,4,5]

def add(a):

    return a+10

mlist=list(map(add,list1))

print(mlist)




#op - [11, 12, 13, 14, 15]


# Map (funt,iterable) funt==arguments:expression

#filter (funt,iterable) funtion ==arguments : conditions


#filter
