n,m=map(int,input().split())
b=[]
c=[0]*(m)
for i in range(n):
    a=list(map(int,input().split()))
    b.append(sum(a))
    for j in range(m):
        c[j]+=a[j]
print(max(b+c))