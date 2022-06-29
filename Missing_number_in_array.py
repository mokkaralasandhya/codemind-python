t=int(input())
for k in range(t):
    s=int(input())
    arr=list(map(int,input().split()))
    for i in range(1,s+1):
        if i not in arr:
            print(i)