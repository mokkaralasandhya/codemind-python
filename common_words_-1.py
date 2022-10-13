s=input()
s=s.lower()
b=input()
b=b.lower()
s=s.split()
b=b.split()
#print(s,b)
c=0
for i in s:
    if i in b:
        c+=1
print(c)