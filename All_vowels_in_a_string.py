s=input()
k='aeiou'
k1='AEIOU'
a=''
a1=''
for i in s:
    if i in k and i not in a:
        a=a+i
for i in s:
    if i in k1 and i not in a1:
        a1=a1+i        
if len(a)==len(k) or len(a1)==len(k1):
    print("True")
else:
    print("False")