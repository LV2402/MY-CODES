l=list(map(int,input().split()))
i=0
for j in range(1,len(l)):
    if l[j]!=l[i]:
        i+=1
        l[i]=l[j]
print(l)
        