def floor(l,x):
    lo,h,ans=0,len(l)-1,-1
    while lo<=h:
        m=(lo+h)//2
        if l[m]<=x:
            ans=m
            lo=m+1
        else:
            h=m-1
    return l[ans]

def ceil(l,x):
    lo,h,ans=0,len(l)-1,len(l)
    while lo<=h:
        m=(lo+h)//2
        if l[m]>=x:
            ans=m
            h=m-1
        else:
            lo=m+1
    return l[ans]

l=[3, 4, 4, 7, 8, 10]
x= 8
print(floor(l,x))
print(ceil(l,x))