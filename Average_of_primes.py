def prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return -2
    else:
        return 2
n=int(input())
arr=list(map(int,input().split()))
c=0
sum=0
for i in range(0,n):
    if prime(arr[i])==2 and arr[i]!=1:
        sum+=arr[i]
        c+=1
avg=sum/c
print("{:.2f}".format(avg))