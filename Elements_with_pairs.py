n=int(input())
sum=0
arr=list(map(int,input().split()))
if n%2!=0:
    arr.append(0)
print(*arr)