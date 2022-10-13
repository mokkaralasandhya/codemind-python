s=input()
s=s.lower()
s1=input()
s1=s1.lower()
a=[]
c=0
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
a=sorted(a)
for i in a:
    print(i,end='')