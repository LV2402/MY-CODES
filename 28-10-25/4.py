def find_gcd(x,y):
    while y:
        x,y=y,x%y
    return x
for _ in range(int(input())):
    size=int(input())
    nums=list(map(int, input().split()))
    common=nums[0]
    for val in nums[1:]:
        common=find_gcd(common,val)
    ans=2
    while find_gcd(ans,common)!=1:
        ans+=1
    print(ans)
