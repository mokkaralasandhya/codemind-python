def pal(s):
    s1=""
    for i in s:
        if i.isupper():
            s1+=i.lower()
        else:
            s1+=i
    if s1==rev(s1):
        return 1
    else:
        return 0
def rev(s):
    s1=""
    for i in range(len(s)-1,-1,-1):
        s1+=s[i]
    return s1
a=input()
arr=list(a.split())
c=0
for i in arr:
    if pal(i)==1:
        c+=1
print(c)