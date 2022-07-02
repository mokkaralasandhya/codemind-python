n=int(input())
t=n
s=0
while t!=0:
    r=t%10
    pro=1
    for i in range(1,r+1):
        pro*=i
    s+=pro
    t//=10
if s==n:
    print("The number %d is a strong number"%n)
else:
    print("The number %d is not a strong number"%n)