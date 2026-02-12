l=list(map(int,input().split()))
for i in range(len(l)-1):
    mini=i
    for j in range(i,len(l)):
        if l[j]<l[mini]:
            mini=j
    l[i],l[mini]=l[mini],l[i]
    print(l)
print(l)