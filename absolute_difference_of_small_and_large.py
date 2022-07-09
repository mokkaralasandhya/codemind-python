n=input()
s=n.split()
sm=0
la=0
for i in s:
    print(abs(ord(min(i))-ord(max(i))),end=" ")