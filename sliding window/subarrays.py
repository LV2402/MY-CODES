l=[9,4,1,7]
n=len(l)
sub=[]
for i in range(n):
    for j in range(i,n):
        t=[]
        for k in range(i,j+1):
            t.append(l[k])
        sub.append(t)
print(sub)