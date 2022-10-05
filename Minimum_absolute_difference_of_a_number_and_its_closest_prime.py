N=int(input())
for i in range(N,2,-1):
    for j in range(2,i):
        if i%j==0:
            #print(i)
            break
    else:
        break
for m in range(N+1,N+100):
    for n in range(2,m):
        if m%n==0:
            #print(i)
            break
    else:
        break
if abs(N-m)>=abs(N-i):
    print(abs(N-i))
else:
    print(abs(N-m))