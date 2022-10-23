s=input()
s=s.lower()
s1=input()
s1=s1.lower()
a=[]
b=[]
for i in range(len(s)):
    if s[i]==' ':
        continue
    if s[i] not in s1 and s[i] not in a:
        a.append(s[i])
for i in range(len(s1)):
    if s1[i]==' ':
        continue
    if s1[i] not in s and s1[i] not in a:
        a.append(s1[i])        
for i in range(len(a)):
    b.append(ord(a[i]))
b=sorted(b)
for i in range(len(b)):
    print(chr(b[i]),end='')