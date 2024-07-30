'''
class edex():
    def __init__(self):
        print("i am constructor")
    def display(self):
        print("i am praveen")
o1=edex()
o1.display()
'''


class mobiles():
    def __init__(self,bname,mname,ram,price):
        print("\twelcome")
        print("---------------------------")
        self.brand=bname
        self.model=mname
        self.ram=ram
        self.price=price
        
    def display(self):
        print("brand name \t:",self.brand)
        print("model name \t:",self.model)
        print("RAM \t\t:",self.ram)
        print("price \t\t:",self.price)
redmi=mobiles("redmi","note 10 pro","6GB",30000)
redmi.display()
vivo=mobiles("vivo","v15 pro","12GB",40000)
vivo.display()
samsung=mobiles("smsung","M22 pro","6GB",30000)
samsung.display()
poco=mobiles("poco","p pro","12GB",50000)
poco.display()
    
    


    
    



    
    
