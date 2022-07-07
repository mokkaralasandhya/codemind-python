n=int(input())
arr=list(map(int,input().split()))
k=n//2
sum1=0
sum2=0
for i in range(0,k):
    sum1+=arr[i]
for i in range(k,n):
    sum2+=arr[i]
l=abs(sum1-sum2)
print(l)

    