n=int(input())
arr=list(map(int,input().split()))
c=0
for i in range(0,n):
    if arr[i]%2==0:
        c+=1
if c==n:
    print("True")
else:
    print("False")