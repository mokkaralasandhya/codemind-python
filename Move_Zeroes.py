n=int(input())
a=list(map(int,input().split()))
s=len(a)
c=0
for i in range(0,s):
    if a[i]!=0:
        a[c]=a[i]
        c+=1
while c<n:
    a[c]=0
    c+=1
print(*a)