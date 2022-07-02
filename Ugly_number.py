x=int(input())
j=0
while x!=1:
    if x%2==0:
        x//=2
    elif x%3==0:
        x//=3
    elif x%5==0:
        x//=5
    else:
        print("Not Ugly Number")
        j=1
        break
if j==0:
    print("Ugly Number")