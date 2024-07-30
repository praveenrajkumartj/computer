class A():
    def display(self):
        print("a class")
class B():
    def display1(self):
        print("b class")
class C():
    def display2(self):
        print("c class")
class D(A,B,C):
    def display3(self):
        print("d class")
o1=D()
o1.display3()
o1.display1()
o1.display2()
o1.display()


print("")        

class A():
    def display(self):
        print("a class")
class B(A):
    def display1(self):
        print("b class")
class C(A):
    def display2(self):
        print("c class")
class D(A):
    def display3(self):
        print("d class")
o1=D()
o2=B()
o3=C()

o1.display3()
o1.display()
o2.display()
o3.display()


print("")        

class A():
    def display(self):
        print("a class")
class B(A):
    def display1(self):
        print("b class")
class C(B):
    def display2(self):
        print("c class")
class D(A):
    def display3(self):
        print("d class")
o1=D()
o2=B()
o3=C()

o2.display()
o2.display1()
o3.display()
o3.display1()
o3.display2()
o1.display()
o1.display3()



        


        


        


        


        




        


        


        


        


        
