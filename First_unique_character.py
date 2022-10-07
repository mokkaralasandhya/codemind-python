s=input()
s=s.lower()
a=0
for i in range(len(s)):
    if s[i]==' ':
        continue
    if s.count(s[i])==1:
        print(s[i])
        a=1
        break
if a==0:
    print(-1)