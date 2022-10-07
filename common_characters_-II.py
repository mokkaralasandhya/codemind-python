s=input()
s1=input()
s=s.lower()
s1=s1.lower()
a=''
for i in s:
    if i==' ':
        continue
    if i in s1 and i not in a:
        a+=i
print(len(a))