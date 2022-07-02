s=input()
c=0
m=0
vo='aeiouAEIOU'
for i in range(len(s)):
    c=0
    for j in range(i,len(s)):
        if s[j] in vo:
            c+=1
            if m<c:
                m=c
        else:
            break
print(m)