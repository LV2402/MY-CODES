a=[3,4,5,6,8,10,12,13,14]
l,h=0,len(a)-1
ans=-1
while l<=h:
    m=(l+h)//2
    if a[m]-m==a[0]:
        ans=a[m]
        l=m+1
    else:
        h=m-1
print(ans+1)