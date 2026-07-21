l=[1,2,3,4,5,6,7,8,9]
x=int(input())
def iterative_binary_search(l,x):
    lo,h=0,len(l)-1
    while lo<=h:
        m=(lo+h)//2
        if l[m]==x:
            return m
        elif l[m]>x:
            h=m-1
        else:
            lo=m+1
    return -1

def recursive_binary_search(l, x, lo, h):
    if lo > h:
        return -1
    m = (lo + h) // 2
    if l[m] == x:
        return m
    elif l[m] > x:
        return recursive_binary_search(l, x, lo, m - 1)
    else:
        return recursive_binary_search(l, x, m + 1, h)

print(iterative_binary_search(l,x))
print(recursive_binary_search(l,x,0,len(l)-1))