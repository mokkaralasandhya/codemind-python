def prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    else:
        return 1
n=int(input())
a=list(map(int,input().split()))
a1=min(a)
a2=max(a)
for i in range(n):
    if a[i]==a1:
        b=i
        break
for i in range(n-1,-1,-1):
    if a[i]==a2:
        b1=i
        break
if b>b1:
    b,b1=b1,b
c=0
for i in range(b,b1+1):
    if a[i]==1:
        continue
    if(prime(a[i])):
        c+=1
print(c)
    