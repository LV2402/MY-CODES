#return number of subarrays containg atmost k odd numbers

def fun(arr,k):
    l=0
    n=len(arr)
    temp=0
    ans=0
    
    for r in range(n):
        if arr[r]%2==1:
            temp+=1
        
        while temp>k :
            if arr[l]%2==1:
                temp-=1
            l+=1
            
        ans+=r-l+1

    return ans

arr=[1,3,4,5,7]
k=2
x=fun(arr,k)
print(x)


# Below formula applicable only when they ask number of sub arrays
#           Exact(k) = Atmost(k)-Atmost(k-1)