#day-05-tasks
#task01 to task 05
print("task-1")


mark=int(input("Enter your score"))
if mark>=90 and mark<=100:
    print("A")
elif mark>=80 and mark<90:
    print("B")
elif mark>=70 and mark<80:
    print("C")
elif mark>=60 and mark<70:
    print("D")
elif mark>=0 and mark<=59:
    print("F")
else:
    print("invaild marks")
print("\n")


print("task-2")

age=int(input("Enter your age"))
if age>0 and age<12:
    print("Your's ticket price is: R.S 5.00/-")
elif age>=12 and age<=64:
    print("Your's ticket price is: R.S 10.00/-")
elif age>=65 and age<120:
    print("Your's ticket price is: R.S 5.00/-")
else:
    print("please enter your correct age.")
print("\n")


print("task-3")

number=int(input("Enter the number:"))
if number==0:
           print("ZERO")
elif number==number>0:
           print("postive number")

else:
           print("negative number")
print("\n")


print("task-4")
char=input("enter the vowel:").lower()
if char=='a' or char=='e' or char=='i' or char=='o' or char=='u':
    print(char ,"is a vowel")
else:
    print(char ,"is a not vowel")
print("\n")


print("task-5")
num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
op=input("enter a operator(+,-,*,/):")
if op=='+':
    print("result:",num1+num2)
elif op=='-':
    print("result:",num1-num2)
elif op=='/':
    if num2==0:
        print(num1,"cannot divide by 0")
    else:
        print("result:",num1/num2)
elif op=='*':
    print("result:",num1*num2)
else:
    print("invaild operation")
print("\n")    
