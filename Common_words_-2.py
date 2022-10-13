s=input()
s=s.lower()
s1=input()
s1=s1.lower()
s=s.split()
s1=s1.split()
c=0
for i in s:
    if s.count(i)==1 and i in s1:
        if s1.count(i)==1:
            c+=1
print(c)     