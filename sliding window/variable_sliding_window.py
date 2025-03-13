#You are given an array and You should Find the maximum length of the subarray which has atmost k ones
arr=list(map(int,input().split()))
k=int(input())
n,temp,l,ans=len(arr),0,0,0
for r in range(n):
    if arr[r]==1:
        temp+=1
    
    while temp>k:
        if arr[l]==1:
            temp-=1
        l+=1
    
    ans=max(ans,r-l+1)
print(ans)