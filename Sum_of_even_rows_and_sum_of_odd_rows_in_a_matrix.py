n,m=map(int,input().split())
ev=0
od=0
for j in range(n):
    m=list(map(int,input().split()))
    for i in m:
        if j%2:
            od+=i
        else:
            ev+=i
print(ev,od)