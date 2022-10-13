s=input()
s=s.lower()
s=s.split()
m=0
a=''
b=[]
k=s[0]
for i in k:
    for j in s:
        if i in j:
            continue
        else:
            break
    else:
        m=1
        a=a+i
for i in a:
   b.append(ord(i))
if m==0:
    print(-1)
else:
 print(chr(min(b)))   