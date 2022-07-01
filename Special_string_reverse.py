s=input()
l=[]
for i in s:
    if ord(i)>=97 and ord(i)<=122:
        l.append(i)
l.reverse()
for i in range(len(s)):
    if not ord(s[i])>=97 and ord(s[i])<=122:
        l.insert(i,s[i])
print(*l,sep="")
    