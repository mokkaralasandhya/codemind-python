s=input()
s=s.lower()
a=[]
b=[]
for i in range(len(s)):
    if s[i]==' ':
        continue
    if s[i] not in a:
        a.append(s[i])
for i in a:
    b.append(ord(i))
b=sorted(b)
for i in b:
    print(chr(i),end='')