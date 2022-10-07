a,b=map(int,input().split())
z=0
x=0
for i in range(a):
    s=list(map(int,input().split()))
    for i in s:
        if i%2==0:
            z+=i
        if i%2!=0:
            x+=i
print(z,x)