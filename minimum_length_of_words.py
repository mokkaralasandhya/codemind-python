n=input()
s=n.split()
c=0
min=1000
for i in s:
    c=len(i)
    if min>c:
        min=c
print(min)