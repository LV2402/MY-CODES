l=[3, 4, 4, 13, 13, 13, 20, 40]
k=4
lo,h,idx=0,len(l)-1,-1
while lo<=h:
    m=(lo+h)//2
    
    if l[m]==k:
        idx=m
        lo=m+1
        
    elif l[m]<k:
        lo=m+1
    
    else:
        h=m-1

print(idx)

# for first occurence if l[m]==k:h=m-1 and idx =m and for last occurence if l[m]==k:lo=m+1 and idx=m

# for total occurence count we should return first occurence + last occurence -1 