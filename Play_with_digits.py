def fun(n):
    c=0
    while(n):
        r=n%10
        c=c+r
        n//=10
    return c
n=int(input())
k=0
a=list(map(int,input().split()[:n]))
for i in a:
    k=k+fun(i)
print(k)