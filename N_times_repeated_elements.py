n=int(input())
arr=list(map(int,input().split()))
b=int(input())
k=[]
for i in range(n):
    if arr.count(arr[i])==b and arr[i] not in k:
        k.append(arr[i])
if len(k)==0:
    print(-1)
else:
    print(*k)