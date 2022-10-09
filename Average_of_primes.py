def fun(n):
    for i in range(2,n):
        if n%i==0:
            return 0
    else:
        return 1
n=int(input())
a=list(map(int,input().split()))
s=0
c=0
for i in a:
    if i==1:
        continue
    if fun(i)==1:
        c+=1
        k=i
        s+=k
print('{:.2f}'.format(s/c))