n=int(input())
c=0
for i in range(1,n+1):
    fact=0
    if n%i==0:
        for j in range(1,i+1):
            if i%j==0:
                fact+=1
    if fact>2:
        c+=1
print(c+1)