n=int(input())
f=0
s=0
c=0
for i in range(1,n+1):
    if(n%i==0):
        f+=1
if f==2:
    while n>0:
        r=n%10
        s+=1
        f=0
        for j in range(1,r+1):
           if r%j==0:
               f+=1
        if f==2:
            c+=1
        n//=10
    if c==s:
        print("Mega Prime")
    else:
        print("Not Mega Prime")
else:
    print("Not Mega Prime")
    