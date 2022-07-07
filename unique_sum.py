n=int(input())
sum=0
arr=list(map(int,input().split()))
for i in range(0,n):
    c=1
    for j in range(0,n):
        if arr[i]!=-1:
            if arr[i]==arr[j] and i!=j:
                c+=1
                arr[i]=-1
    if c==1:
        sum+=arr[i]
print(sum)