'''
class cal():
    a=5
    b=3
    def add():
        print(cal.a +cal.b)    

     
        
    
        
    def sub():
        print(cal.a -cal.b)    

     
        
        
        
    def  mul():
        print(cal.a *cal.b)    

     
 
    def  div():
       print(cal.a /cal.b)    

     

cal.add()
cal.sub()
cal.mul()
cal.div()




class cal():
    a=5
    b=3
    def add(self):
        print("hell0")
    def sub(self):
        print(self.a -self.b)    
edex=cal()
edex.add()
edex.sub()
'''
'''
a=int(input("enter the a value:"))
b=int(input("enter the a value:"))

class call():

    def add(self,a,b):
        print("addtion of ",a,"and", b,":",a +b)    

     
        
    
        
    def sub(self,a,b):
        print("addtion of ",a, "and", b,":",a -b)
e=call()
e.add(a,b)
e.sub(a,b)
'''



a=int(input("enter the a value:"))
b=int(input("enter the a value:"))
print("\nadd\nsub\nmul\ndiv")
choose=input("choose the function:").lower()

class call():


    def values(self,a,b):
        self.a=a
        self.b=b

    def add(self):
        print("addtion of ",self.a,"and",self.b,":",self.a +self.b)    

        
    def sub(self):
        print("subraction of ",self.a, "and",self. b,":",self.a -self.b)
    def mul(self):
        print("multiplication of ",self.a, "and",self. b,":",self.a *self.b)
    def div(self):
        print("division of ",self.a, "and",self. b,":",self.a /self.b)
    
    
        
e=call()
e.values(a,b)

if choose=="add":
    e.add()
    
elif choose=="sub" :
    e.sub()
elif choose=="mul" :
    e.mul()
elif choose=="div" :
    if b==0:
        print("0 is not divisib;e")
    else:
         e.div() 
      
    
else:
    print("invaild function")
     
        
        
    


             
       
     
        
    
        
    





     
        
    
        
    





