l=[3,4,5,1,2]
lo,h,=0,len(l)-1
mini=l[(lo+h)//2]

while lo<=h:
    m=(lo+h)//2
    
    if l[lo]<=l[m]:
        mini=min(mini,l[lo])
        lo=m+1
    
    else:
        mini=min(mini,l[m])
        h=m-1

print(mini)