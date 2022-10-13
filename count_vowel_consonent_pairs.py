s=input()
s=s.lower()
k=s[::-1]
a='aeiouAEUIO'
c=0
for i in range((len(s)//2)):
    if s[i] in a and k[i] not in a:
        if s[i]!=' ':
            if k[i]!=' ':
              c+=1
    elif s[i] not in a and k[i] in a:
        if s[i]!=' ':
            if k[i]!=' ':
              c+=1
print(c)        