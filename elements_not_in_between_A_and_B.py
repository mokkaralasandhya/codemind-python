n=int(input())
a=list(map(int,input().split()))
x,y=map(int,input().split())
k=0
max=0
for i in range(n):
    if a[i]<x or a[i]>y:
        k=1
        print(a[i],end=' ')
if k==0:
    print(-1)
