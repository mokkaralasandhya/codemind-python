s=input()
s1=input()
s=s.lower()
s1=s1.lower()
s=s.split()
s1=s1.split()
c=[]
for i in s1:
    if i in s:
        c.append(i)
print(*c)