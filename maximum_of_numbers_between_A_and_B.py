n=int(input())
arr=list(map(int,input().split()))
a,b=map(int,input().split())
max=0
c=0
for i in range(n):
    if arr[i]>=a and arr[i]<=b:
        c+=1
        if arr[i]>max:
            max=arr[i]
if c==0:
    print(-1)
else:
    print(max)