a=input()
b=list(map(int,input().split()))
for i in range(0,len(b)):
    for j in range(i+1,len(b)):
        if(b[i]==b[j]):
            print(b[j])