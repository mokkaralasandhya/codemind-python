n=int(input())
s=n*n
sum=0
while s>0:
    sum=sum+s%10
    s//=10
if(sum==n):
    print("Neon Number")
else:
    print("Not Neon Number")