for i in range(int(input())):
    s=input()
    s1=input()
    c=0
    for i in range(len(s)):
        if ord(s[i])<=ord(s1[i]):
            c+=1
    if c==len(s):
        print("YES")
    else:
        print("NO")