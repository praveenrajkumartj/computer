print("D-MART")
print("--------------------------------------------------------------------------------------------------------------------")
print("PRODUCT LIST")
product={"mobile":["redmi","vivo","oppo"],
         "tv":["sony","lg","samsung"],
         "laptop":["accer","lenova","asus"]
          
    }
for i,j in product.items():
    print(i,end="\t\t\t")
print()
pick1=input("pick any one :")

if pick1=="mobile":
    for i in product.get("mobile"):
        print(i,end="\t")

   
