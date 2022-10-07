n=int(input())
a=list(map(int,input().split()))
k=[]
for i in range(n):
    max=0
    if(i==n-1):
        k.append(-1)
        continue
    for i in range(i+1,n):
        if(a[i]>max):
            max=a[i]
    k.append(max)
print(*k)