#Write a Python program to find the count of subarrays of size k in a given list whose average is greater than or equal to t.
arr = list(map(int, input().split()))
k, t = map(int, input().split())
n = len(arr)
c = 0
l=0
temp=0
for r in range(n):
    temp+=arr[r]
    if r-l==k:
        temp-=arr[l]
        l+=1
    if r-l+1==k:
        if temp/k>=t:
            c+=1
print(c)