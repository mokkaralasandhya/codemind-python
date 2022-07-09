n=input()
c=0
for i in n:
    if ord(i)!=32:
        c+=1
    if ord(i)==32:
        print(c,end=' ')
        c=0
else:
    print(c,end=" ")