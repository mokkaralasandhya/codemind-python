n=int(input())
a=list(map(int,input().split()))
f=0
for i in range(3,len(a)):
    if a[i-1]+a[i-2]==a[i]:
        f+=1
if f+3==n:
    print("yes")
else:
    print("no")