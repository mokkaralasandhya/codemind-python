def fun(n):
    for i in range(2,n):
        if n%i==0:
            return 0
    else:
        return 1
n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(n):
    if a[i]==1:
        continue
    if fun(a[i]):
        c+=1
print(c)