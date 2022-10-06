n=int(input())
a=list(map(int,input().split()))
c=k=0
for i in range(0,n-2,2):
    if(a[i]>a[i+1] and a[i]>a[i-1]) or (a[i]<a[i+1] and a[i]<a[i-1]):
        c+=1
    else:
        k+=1
if k==0:
    print(c)
else:
    print(-1)