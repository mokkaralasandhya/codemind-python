def fun(n):
    c=0
    if n<0:
        n=n*(-1)
    if n==0:
        return 1
    while(n):
        r=n%10
        c+=1
        n//=10
    return c
m,n=map(int,input().split())
a=list(map(int,input().split()))
c=0
for i in a:
    k=fun(i)
    if k==n:
        c+=1
print(c)