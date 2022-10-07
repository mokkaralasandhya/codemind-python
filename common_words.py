s=input()
s=s.lower()
s1=input()
s=s.split()
s1=s1.split()
k=[]
for i in s1:
    if i in s:
        k.append(i)
print(*k)