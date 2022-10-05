n=int(input())
a=list(map(int,input().split()))
b=[]
b1=a[::-1]
for i in range(n//2):
    b.append(a[i])
    b.append(b1[i])
if n%2!=0:
    b.append(a[n//2])
    b.append(0)
print(*b)