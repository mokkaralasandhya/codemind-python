n=int(input())
a=list(map(int,input().split()))
x,y=map(int,input().split())
k=0
min=9989
for i in range(n):
    if a[i]<x or a[i]>y:
        k=1
        if a[i]<min:
            min=a[i]
if k==0:
    print(-1)
else:
    print(min)