l=int(input())
n=int(input())
w=[]
h=[]
for i in range(0,n):
    e1,e2=map(int,input().split())
    w.append(e1)
    h.append(e2)
for i in range(0,n):
    if w[i]>=l and h[i]>=l:
        if w[i]==h[i]:
            print("ACCEPTED")
        else:
            print("CROP IT")
    else:
        print("UPLOAD ANOTHER")
