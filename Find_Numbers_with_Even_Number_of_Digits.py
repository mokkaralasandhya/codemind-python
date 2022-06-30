n=int(input())
a=list(map(str,input().split()))
c=0
for i in a:
    a=len(i)
    if a%2==0:
        c=c+1
print(c)
        