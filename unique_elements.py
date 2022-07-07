n=int(input())
arr=list(map(int,input().split()))
k=[]
for i in range(n):
    if arr[i] not in k:
        k.append(arr[i])
print(*k)