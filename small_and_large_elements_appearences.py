s=input()
b=[]
min=999
for i in s:
    b.append(ord(i))
a=max(b)
a1=b.index(a)
for i in b:
    if min>i and i!=32:
        min=i
c=b.index(min)
print(s[c],s.count(s[c]),s[a1],s.count(s[a1]))