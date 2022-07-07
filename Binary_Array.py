n=int(input())
arr=list(map(int,input().split()))
c=0
for i in range(0,n):
    if arr[i]==0 or arr[i]==1:
        c=c+1
if c==n:
    print("True")
else:
    print("False")