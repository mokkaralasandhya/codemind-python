s=input()
s=s.lower()
a=[]
for i in range(len(s)):
    if s[i]==' ':
        continue
    if s[i] not in a:
        a.append(s[i])
print(len(a))