t=int(input())
k=0
for i in range(t):
    s=input()
    s=list(s)
    s1=''
    for i in range(len(s)):
        if s[i]==chr(88):
            continue
        s1=s1+s[i]
    if s1=='--':
        k=k-1
    else:
        k=k+1
print(k)    