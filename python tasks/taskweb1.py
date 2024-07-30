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
print("--------------------------------------------------------------------------------------------------------------------")
if pick1 in product:
    for i,j in product.items():
        if i==pick1:
            print(pick1)
            for x in j:
                print(x,end="\t\t\t")
else:
    print("not in stock")
    
     
            
brands={"redmi":{"brand name":"redmi",
                 "model name":"note 10 pro",
                 "price":20000,
                 "GST":10,
                 "final price":22000
                   },
        "vivo":{"brand name":"vivo",
                 "model name":"vivo V23",
                 "price":30000,
                 "GST":10,
                 "final price":33000
                },
        "oppo":{"brand name":"oppo",
                 "model name":"oppo F11",
                 "price":40000,
                 "GST":10,
                 "final price":44000
                },
        "sony":{"brand name":"sony",
                 "model name":"sony LCD HDR10",
                 "price":30000,
                 "GST":10,
                 "final price":33000
                },
        "lg":{"brand name":"LG",
                 "model name":"LG LED HDR10",
                 "price":20000,
                 "GST":10,
                 "final price":22000
                },
        "samsung":{"brand name":"samsung",
                 "model name":"SAMSUNG LED HDR10+",
                 "price":40000,
                 "GST":10,
                 "final price":44000
                },
        "accer":{"brand name":"accer",
                 "model name":"accer ultran",
                 "price":40000,
                 "GST":10,
                 "final price":44000
                },
        "lenova":{"brand name":"lenova",
                 "model name":"lenova gaming laptop",
                 "price":50000,
                 "GST":10,
                 "final price":55000
                },
        "asus":{"brand name":"lenova",
                 "model name":"lenova gaming laptop",
                 "price":60000,
                 "GST":10,
                 "final price":66000
                }
    }

print()
pick2=input("pick any one :")
for i,j in brands.items():
    if i==pick2:
        print(pick2)
        for x,y in j.items():
            print(x,y,sep=":")


print("buy now","close",sep="\t"*4)
print("-------"*20)
pick3=input("pick any one")


            
        
            

       
            
                   
                   
                   
                   
            
        
            
    
