a=input()
b=[]
for i in range(len(a)):
    if a[i] not in b:
        b.append(a[i])
        c=b
for i in c:
    if i in 'aeiouAEIOU':
        print(i,end=' ')