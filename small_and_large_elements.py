l=list(map(str,input().split()))
a=[]
mi=min(l[0])
ma=max(l[len(l)-1])
a.append(mi)
a.append(ma)
print(*a)