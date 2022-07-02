t=int(input())
for i in range(t):
    s=input()
    c=0
    l=len(s)
    for j in range(l):
        if s[j]==s[l-j-1]:
            c=1
        else:
            c=0
            break
    if c==1:
        if len(s)%2==0:
            print("YES EVEN")
        else:
            print("YES ODD")
    else:
        print("NO")