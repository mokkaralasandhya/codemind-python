m,n=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
for i in range(m):
    if a[i] not in b:
        d=a[i]
        print(d,end=' ')
for i in range(n):
    if b[i] not in a:
        c=b[i]
        print(c,end=' ')