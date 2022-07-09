n=input()
s=n.split()
sm=0
la=0
for i in s:
    sm+=ord(min(i))
    la+=ord(max(i))
print(la-sm)