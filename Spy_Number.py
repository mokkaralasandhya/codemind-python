n=int(input())
temp=n
sum=0
p=1
while temp>0:
    lastdigit=temp%10
    sum+=lastdigit
    p*=lastdigit
    temp//=10
if sum==p:
    print("Spy Number")
else:
    print("Not Spy Number")