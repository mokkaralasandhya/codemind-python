import math
n=int(input())
a=list(map(int,input().split()))
s=0
for i in range(n):
    if a[i]>=0:
        sr=int(math.sqrt(a[i]))
        if sr*sr==a[i]:
            s+=a[i]
print(s)