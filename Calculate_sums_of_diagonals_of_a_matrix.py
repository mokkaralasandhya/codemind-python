n=int(input())
s1,s2=0,0
t=n-1
for i in range(n):
    l=list(map(int,input().split()))
    s1+=l[i]
    s2+=l[t]
    t-=1
print("Principal Diagonal:%d"%s1)
print("Secondary Diagonal:%d"%s2)