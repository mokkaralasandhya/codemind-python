n=int(input())
a=list(map(int,input().split()))
b=int(input())
c=max(a)
d=0
for i in range(n):
    k=a[i]+b
    if k>=c:
        print(True,end=' ')
    else:
        print(False,end=' ')