def fun(n):
    c=0
    while(n):
        r=n%10
        c+=1
        n//=10
    return c
a=int(input())
x=list(map(int,input().split()))
f=[]
for i in x:
    f.append(fun(i))
m=max(f)
print(f.count(m))