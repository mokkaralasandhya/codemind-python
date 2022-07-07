n=int(input())
arr=list(map(int,input().split()))
a,b=map(int,input().split())
c=0
for i in range(n):
    if arr[i]>=a and arr[i]<=b:
        c+=1
        print(arr[i],end=" ")
if c==0:
    print(-1)
    