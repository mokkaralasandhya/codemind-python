s=input()
p=input()
c=0
for i in s:
    if i in p:
        c+=1
if c==0:
    print(-1)
else:
    print(c)