def fun(n):
    s=0
    while(n):
        r=n%10
        s=s*10+r
        n//=10
    return s
n=int(input())
b=list(map(int,input().split()))
for s in b:
    print(fun(s),end=' ')