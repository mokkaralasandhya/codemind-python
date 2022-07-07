n=int(input())
arr=list(map(int,input().split()))
sum=0
for i in range(0,n):
    sum+=arr[i]
ave=sum//n
c=0
for i in range(0,n):
    if arr[i]>=ave:
        c=c+1
print(c)