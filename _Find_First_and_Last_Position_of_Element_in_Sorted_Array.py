n=int(input())
a=list(map(int,input().split()))
s=int(input())
flag=0
l=(sorted(a))
for i in range(n):
    if l[i]==s:
        print(i,end=' ')
        flag=1
        break
for i in range(n-1,-1,-1):
    if l[i]==s:
        print(i,end=' ')
        flag=1
        break
if flag==0:
    print(-1,-1)