s=input()
s=s.lower()
s=s.split()
a='aeiou'
c=0
for i in s:
    for j in range(len(i)):
        k=i[::-1]
        if i[j] in a and k[j] not in a:
            c+=1
        elif i[j] not in a and k[j] in a:
              c+=1
print(c//2)     