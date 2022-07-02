n=int(input())
s=0
pro=1
while n>0:
    r=n%10
    s+=r
    pro*=r
    n//=10
print(pro-s)