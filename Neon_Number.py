a=int(input())
sum=0
p=a*a
while p>0:
    rem=p%10
    sum+=rem
    p//=10
if sum==a:
    print("Neon Number")
else:
    print("Not Neon Number")