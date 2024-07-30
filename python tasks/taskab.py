print("D-MART")
print("------------------------------------------------------------")
print("PRODUCTS LISTS")
dic={"product1":"1)mobile","proct2":"2)tv","product3":"3)laptops"}

for i in dic.values():
    print(i,end="\t")
print("\n")
cp=input("choose any one in the products :").lower()
print("------------------------------------------------------------")
if cp=="mobile":
    print("MOBILES LISTS")
    dic1={"mobile1":"1)oneplus","mobile2":"2)apple","mobile3":"3)redmi"}
    for i in dic1.values():
        print(i,end="\t\t")
    print("\n")   
    cm=input("choose any one in the mobile products :").lower()
    print("------------------------------------------------------------")
    if cm=="oneplus":
        print("ONEPLUS MOBILE\nRAM:12GB\nINTERNAL STORAGE:256\nBATTERY CAPACITY:5000mAh\nMOBILE PRICE:30,000\nGST 18%:5,400\nTOTAL PRICE =RS.35,400")
    elif cm=="apple":
        print("APPLE MOBILE\nRAM:12GB\nINTERNAL STORAGE:256\nBATTERY CAPACITY:3500mAh\nMOBILE PRICE:80,000\nGST 18%:14,400\nTOTAL PRICE =RS.94,400")
    elif cm=="redmi":
        print("REDMI MOBILE\nRAM:12GB\nINTERNAL STORAGE:256\nBATTERY CAPACITY:5000mAh\nMOBILE PRICE:20,000\nGST 18%:3,600\nTOTAL PRICE =RS.23,600")
    else:
        print("IT IS NOT IN THE MOBILE PRODUCTS LIST.")
elif cp=="laptop":
    print("LAPTOPS LISTS")
    dic2={"laptop1":"1)accer","laptop2":"2)apple","laptop3":"3)redmi"}
    for i in dic2.values():
        print(i,end="\t\t")
    print("\n")   
    cl=input("choose any one in the laptop products :").lower()
    print("------------------------------------------------------------")
    if cl=="accer":
        print("ACCER LAPTOP\nRAM:12GB\nINTERNAL STORAGE:256\nBATTERY CAPACITY:5000mAh\nLAPTOP PRICE:30,000\nGST 18%:5,400\nTOTAL PRICE =RS.35,400")
    elif cl=="apple":
        print("APPLE LAPTOP\nRAM:12GB\nINTERNAL STORAGE:256\nBATTERY CAPACITY:3500mAh\nLAPTOP PRICE:80,000\nGST 18%:14,400\nTOTAL PRICE =RS.94,400")
    elif cl=="redmi":
        print("REDMI LAPTOP\nRAM:12GB\nINTERNAL STORAGE:256\nBATTERY CAPACITY:5000mAh\nLAPTOP PRICE:40,000\nGST 18%:7,200\nTOTAL PRICE =RS.47,200")
    else:
        print("IT IS NOT IN THE LAPTOP PRODUCTS LIST.")        
elif cp=="tv":
    print("TV LISTS")
    dic3={"tv1":"1)sony","tv2":"2)pansonic","tv3":"3)redmi"}
    for i in dic3.values():
        print(i,end="\t\t")
    print("\n")   
    ct=input("choose any one in the tv products :").lower()
    print("------------------------------------------------------------")
    if ct=="sony":
        print("SONY TV\nDISPLAY SIZE:82 INCHES \nPANNEL:HDR 10\nDISPLAY TECHNOLOGY:LED\nTV PRICE:80,000\nGST 18%:14,400\nTOTAL PRICE =RS.94,400")
    elif ct=="pansonic":
        print("PANSONIC TV\nDISPLAY SIZE:32 INCHES \nPANNEL:HDR 10+\nDISPLAY TECHNOLOGY:LCD\nTV PRICE:20,000\nGST 18%:3,600\nTOTAL PRICE =RS.23,600")
    elif ct=="redmi":
        print("REDMI TV\nDISPLAY SIZE:52 INCHES \nPANNEL:HDR 400\nDISPLAY TECHNOLOGY:LED\nTV PRICE:30,000\nGST 18%:5,400\nTOTAL PRICE =RS.35,400")
    else:
        print("IT IS NOT IN THE TV PRODUCTS LIST.")
else:
    print("IT IS NOT FOUND IN PRODUCT LIST")

    
    
