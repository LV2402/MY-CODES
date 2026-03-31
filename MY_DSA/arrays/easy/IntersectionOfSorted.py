l=list(map(int,input().split()))
nl=list(map(int,input().split()))
i,j=0,0
t=[]
while i<len(l) and j<len(nl):
    if l[i]<nl[j]:
        i+=1
    elif l[i]>nl[j]:
        j+=1
    else:
        t.append(l[i])
        i+=1
        j+=1
print(t)