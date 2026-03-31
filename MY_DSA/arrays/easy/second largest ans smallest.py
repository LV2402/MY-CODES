l=list(map(int,input().split()))
m1,m2=float("-inf"),float("-inf")
l1,l2=float("inf"),float("inf")
for i in range(len(l)):
    if l[i]>m1:
        m2=m1
        m1=l[i]
    elif l[i]>m2 and l[i]!=m1:
        m2=l[i]
    if l[i]<l1:
        l2=l1
        l1=l[i]
    elif l[i]<l2 and l[i]!=l1:
        l2=l[i]
    
print(m1,m2)
print(l1,l2)