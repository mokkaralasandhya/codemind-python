n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(n-2):
    if a[i]%2==0 and a[i+2]%2!=0:
        c+=1
    elif a[i]%2!=0 and a[i+2]%2==0:
        c+=1
print(c)