def rev(n):
    re=0
    while(n>0):
        l=n%10
        re=(re*10)+l
        n=n//10;
    return re
a=int(input())
c=0
if a<0:
    c=1
    a*=-1
res=rev(a)
if c==1:
    print(res*-1)
else:
    print(res)