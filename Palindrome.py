num=int(input())
su=0
temp=num
while(num>0):
    m=num%10
    su=(su*10)+m
    num=num//10
if su==temp:
    print("True")
else:
    print("False")