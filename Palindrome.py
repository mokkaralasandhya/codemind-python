a=int(input())
temp=a
rev=0
while a>0:
    dig=a%10
    rev=rev*10+dig
    a//=10
if(temp==rev):
    print("True")
else:
    print("False")