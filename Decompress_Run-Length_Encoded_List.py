n=int(input())
a=list(map(int,input().split()))
k=[]
for i in range(0,n-1,2):
    for j in range(a[i]):
        k.append(a[i+1])
print(*k)