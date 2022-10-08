def fun(n):
    s=0
    while(n>0):
        r=n%10
        s+=r
        n//=10
    return s
n=int(input())
a=list(map(int,input().split()))
s=0
for i in a:
    c=fun(i)
    s+=c
print(s)