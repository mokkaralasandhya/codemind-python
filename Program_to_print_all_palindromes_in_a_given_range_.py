a=int(input())
b=int(input())
for i in range(a,b+1):
    temp=i
    s=0
    while i>0:
        r=i%10
        s=(s*10)+r
        i//=10
    if temp==s:
        print(temp,end=' ')