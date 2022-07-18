n=int(input())
arr=list(map(int,input().split()))
c=0
for i in range(len(arr)):
    c=0
    for j in range(i+1,n):
        if(arr[i]==arr[j]):
            c=1
            arr[j]=-1
    if c==1:
        arr[i]=-1
for i in range(len(arr)):
    if arr[i]==-1:
        continue
    else:
        c=1
        print(arr[i],end=" ")
if c==0:
    print("-1")