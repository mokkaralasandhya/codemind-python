a=int(input())
for i in range(1,a+1):
    for j in range(1,a+1):
        if(i==j or j==a-i+1):
            print(a-i+1,end=" ")
        else:
            print(' ',end="")
    print()