l=[4, 5, 6, 7, 0, 1, 2]
k=0
lo,h,idx=0,len(l)-1,False

while lo<=h:
    m=(lo+h)//2
    if l[m]==k:
        idx=True
        break
    
    # elif l[lo]==l[m] and l[m]==l[h]:
    #     lo+=1
    #     h-=1
    
    elif l[lo]<=l[m]:
        if l[lo]<=k and l[m]>=k:
            h=m-1
        else:
            lo=m+1
    
    else:
        if l[m]<=k and k<=l[h]:
            lo=m+1
        else:
            h=m-1

if idx:print("element exists")

#if duplicates are present then we can not decide which part is sorted 
# so we shrink the search space by lo+=1 and h-=1
# but this will increase the time complexity to O(n) in worst case when all elements are same and in average case it will be o(n/2) when half of the elements are same and other half are different
# code has been commented above