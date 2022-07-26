n=int(input())
arr=list(map(int,input().split()))
k=[]
p=[]
r=[]
for i in range(n):
    if arr[i] not in k:
        k.append(arr[i])
        p.append(arr.count(arr[i]))
for i in range(len(k)):
    print(k[i],p[i],end=" ")