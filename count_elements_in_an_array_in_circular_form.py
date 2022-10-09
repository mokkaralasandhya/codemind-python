n=int(input())
a=list(map(int,input().split()))
a.append(a[0])
a.append(a[1])
c=0
for i in range(n):
    if a[i]%2==0 and a[i+2]%2!=0:
        c+=1
    elif a[i]%2!=0 and a[i+2]%2==0:
        c+=1
print(c)