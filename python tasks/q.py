
#11.inverse pyramid
n=int(input())
for i in range(n,0,-1):
    print(""*(2*(n-i)),end="")
    
    for j in range(1,2*i):
        print(j,"" ,end="")
    print()
