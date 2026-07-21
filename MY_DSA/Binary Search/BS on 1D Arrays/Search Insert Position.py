l=[1,2,2,3]
x=2
lo,h,ans=0,len(l)-1,len(l)
while lo<=h:
    m=(lo+h)//2
    if l[m]>=x:
        ans=m
        h=m-1
    else:
        lo=m+1
print(ans)