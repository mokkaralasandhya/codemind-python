n=input()
n=n.lower()
c=0
for i in range(len(n)):
    s=0
    for j in range(len(n)):
        if n[i]==n[j] and n[i]!=' ':
            s+=1
    if s==1:
        c+=1
print(c)