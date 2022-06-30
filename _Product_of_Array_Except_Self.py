n=int(input())
l=list(map(int,input().split()))
s=len(l)
for i in range(s):
    pr=1
    for j in range(s):
        if(i!=j):
            pr*=l[j]
    print(pr,end=" ")
