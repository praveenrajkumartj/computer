class atm():
    def __init__(self,acc,bal):
        print("\twelcome")
        print("--"*20)
        self.account=acc
        self.balance=bal
        
    def display(self):
        print("account no :",self.account)
        print("balance    :",self.balance)
        choose=input("Deposit/ withdraw :").lower()
        if choose=="deposit":
            print("\tdeposit")
            print("--"*20)
            amt=int(input("enter the amount :"))
            print("--"*20)
            print("account no :",self.account)
            print("balance    :",amt+self.balance)
        elif choose=="withdraw":
            
            print("\twithdraw")
            print("--"*20)
            amt=int(input("enter a amount :"))
            if amt>self.balance:
                
                print("--"*20)
                print("account no :",self.account)
                 
                print("balance    : insufficent balance")
            else:
                print("--"*20)
                print("account no :",self.account)
                print("balance    :",self.balance-amt)
        else:
            print("--"*20)
            print("invaild function")
           
                
                
            
             
           
            
deposit=atm("12345678",1000)
deposit.display()

        
        
    
