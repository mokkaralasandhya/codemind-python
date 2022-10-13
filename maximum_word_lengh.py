s=input()
b=[]
s=s.split()
for i in s:
    b.append(len(i))
print(max(b))