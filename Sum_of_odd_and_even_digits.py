import math
n=int(input())
a=list(map(int,input().split()))
s=len(a)
os=0;es=0
res=0
for i in range(0,s):
    if i%2!=0:
        os=os+a[i]
for i in range(0,s):
    if i%2==0:
        es=es+a[i]
res=abs(os-es)
if res==0:
    print("YES")
else:
    print("NO")