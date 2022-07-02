l,r,k=map(int,input().split())
su=0
for i in range(l,r+1):
    if(i%k==0):
        su+=1
print(su)