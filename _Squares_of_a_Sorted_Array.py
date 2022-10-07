n=int(input())
a=list(map(int,input().split()))
for i in range(n):
    if a[i]<0:
        a[i]*=(-1)
b=sorted(a)
for i in b:
    print(i*i,end=' ')