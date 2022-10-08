def fun(n):
    c=0
    while(n):
        r=n%10
        c+=1
        n//=10
    return c
x=int(input())
a=list(map(int,input().split()))
f=[]
for i in a:
    f.append(fun(i))
m=min(f)
print(f.count(m))