def fun(n):
    c=0
    while(n):
        if n<0:
            n=n*(-1)
        r=n%10
        c+=1
        n//=10
    return c
a=int(input())
x=list(map(int,input().split()))
f=[]
#print(x)
for i in x:
    f.append(fun(i))
m=max(f)
for i in range(a):
    if f[i]==m:
        print(x[i],end=' ')