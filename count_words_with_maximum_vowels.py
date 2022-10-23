s=input()
s=s.lower()
s=s.split()
a='aeiou'
b=[]
for i in s:
    c=0
    for j in i:
        if j in a:
            c+=1
    b.append(c)
k=max(b)
print(b.count(k))