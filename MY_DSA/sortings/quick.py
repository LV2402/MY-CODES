def quickSort(l,low,high):
    if low<high:
        part=partition(l,low,high)
        quickSort(l,low,part-1)
        quickSort(l,part+1,high)

def partition(l,low,high):
    p=low
    i,j=low,high
    while i<j:
        while l[i]<=l[p] and i<=high-1:
            i+=1
        while l[j]>l[p] and i>=low+1:
            j-=1
        if i<j:
            l[i],l[j]=l[j],l[i]
    l[j],l[p]=l[p],l[j]
    return j

l=list(map(int,input().split()))
quickSort(l,0,len(l)-1)
print(l)