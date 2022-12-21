s=input()
s=s.lower()
x=''
for i in s:
    if s.count(i)==1 and i!=' ':
        x+=i
x=(sorted(x))
s=''
for i in x:
    s+=i
print(s)