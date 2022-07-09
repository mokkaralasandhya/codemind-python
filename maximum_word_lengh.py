n=input()
s=n.split()
c=0
max=0
for i in s:
    c=len(i)
    if max<c:
        max=c
print(max)