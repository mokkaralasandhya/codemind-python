n=int(input())
f=0
rev=0
for i in range(1,n+1):
    if(n%i==0):
        f+=1
if f==2:
    f=0
    while n>0:
        r=n%10
        rev=(rev*10)+r
        n//=10
    for j in range(1,rev+1):
        if rev%j==0:
            f+=1
    if f==2:
        print("circular prime")
    else:
        print("prime but not a circular prime")
else:
    print("not prime")