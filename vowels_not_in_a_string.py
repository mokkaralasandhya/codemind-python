s=input()
s=s.lower()
a='aeiou'
k=''
m=0
for i in s:
    if i in a:
       k=k+i
for i in a:
    if i not in k:
        m=1
        print(i,end=' ')
if m==0:
    print(0)