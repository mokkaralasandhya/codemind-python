n=input()
s=input()
c=0
for i in range(len(n)):
    if n[i]==s[0]:
        c+=1
        d=i
        break
if c>0:
    print("True")
    print(d)
else:
    print("False")