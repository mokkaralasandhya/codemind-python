t=int(input())
for j in range(t):
    k=0
    a,b,c,d=map(int,input().split())
    for i in range(1,a+1):
        if(i%b==0 and i%c!=0):
            k+=1
        elif(i%b!=0 and i%c==0):
            k+=1
        if(k==d):
            print("Win")
            break
    else:
        print("Lose")