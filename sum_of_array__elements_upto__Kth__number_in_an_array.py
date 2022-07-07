n=int(input())
arr=list(map(int,input().split()))
k=int(input())
sum=0
for i in range(0,n):
    if arr[i]<=k:
        sum+=arr[i]
print(sum)

    