l=list(map(int,input().split()))
nl=list(map(int,input().split()))
i,j=0,0
t=[]
while i<len(l) and j<len(nl):
    if l[i]<nl[j]:
        if not t or t[-1]!=l[i]:
            t.append(l[i])
        i+=1
    else:
        if not t or t[-1]!=nl[j]:
            t.append(nl[j])
        j+=1
    
while i<len(l):
    if not t or t[-1]!=l[i]:
        t.append(l[i])
    i+=1
    
while j<len(nl):
    if not t or t[-1]!=nl[j]:
        t.append(nl[j])
    j+=1
    
print(t)