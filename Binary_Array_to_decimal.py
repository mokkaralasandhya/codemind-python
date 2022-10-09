n=int(input())
a=list(map(int,input().split()))
a=a[::-1]
s=0
k=0
for i in a:
    s+=(i*(2**k))
    k+=1
print(s)