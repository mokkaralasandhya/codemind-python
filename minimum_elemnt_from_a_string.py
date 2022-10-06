s=input()
s=s.split()
a=[]
for i in s[len(s)-1]:
    if ord(i)==32:
        continue
    a.append(ord(i))
k=min(a)
if chr(k+32) in s[len(s)-1]:
    print(chr(k+32))
else:
    print(chr(k))