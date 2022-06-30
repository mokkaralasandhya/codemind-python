n=int(input())
a=list(map(int,input().split()))
ma=0;r=10000
for i in a:
    c=0
    for j in a:
        if i==j:
            c+=1
    if c>ma:
        ma=c
        r=i
    if c==ma:
        if i>r:
            r=i
print(r)
        