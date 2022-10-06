def fun(n):
    s=0
    t=n
    while(n):
        r=n%10
        s=s*10+r
        n//=10
    if s==t:
        return True
    else:
        return False
n=int(input())
c=0
a=list(map(int,input().split()))
for s in a:
    if fun(s):
        c+=1
print(c)