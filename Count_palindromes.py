def fun(n):
    s=0
    t=n
    while(n):
        s=s*10+(n%10)
        n//=10
    if s==t:
        return True
    else:
        return False
n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    if fun(i):
        c+=1
print(c)