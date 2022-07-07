n=int(input())
arr=list(map(int,input().split()))
sum=0
k=0
for i in range(n-1,-1,-1):
    sum=sum+(2**k)*arr[i]
    k+=1
print(sum)