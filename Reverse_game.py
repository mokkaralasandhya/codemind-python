def fun(n):
    s=0
    while(n>0):
        r=n%10
        s=s*10+r
        n//=10
    return s
n=int(input())
a=list(map(int,input().split()))
for i in a:
    print(fun(i),end=' ')