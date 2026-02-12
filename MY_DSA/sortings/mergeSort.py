def mergeSort(l,lo,hi):
    if lo>=hi:return
    
    mid=(lo+hi)//2
    mergeSort(l,lo,mid)
    mergeSort(l,mid+1,hi)
    merge(l,lo,mid,hi)
    
def merge(l,lo,mid,hi):
    t=[]
    left=lo
    right=mid+1
    while left<=mid and right<=hi:
        if l[left]<l[right]:
            t.append(l[left])
            left+=1
        else:
            t.append(l[right])
            right+=1
    while left<=mid:
        t.append(l[left])
        left+=1
    while right<=hi:
        t.append(l[right])
        right+=1
    for i in range(len(t)):
        l[lo + i] = t[i]
        
    
l=list(map(int,input().split()))
mergeSort(l,0,len(l)-1)
print(l)