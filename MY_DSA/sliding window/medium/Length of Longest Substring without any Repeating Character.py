s="cadbzabcd"
maxs=0
# brute force
# for i in range(len(s)):
#     h=[0]*256
#     for j in range(i,len(s)):
#         if h[ord(s[j])]==1:
#             break
#         l=j-i+1
#         maxs=max(maxs,l)
#         h[ord(s[j])]=1
# print(maxs)
# TC: O(n^2) SC:O(256)

# optimal
l,r,maxl=0,0,0
h=[-1]*256
while r<len(s):
    if h[ord(s[r])]!=-1:
        if h[ord(s[r])]>=l:
            l=h[ord(s[r])]+1
        l=max(l,h[ord(s[r])]+1)
    h[ord(s[r])]=r
    maxl=max(maxl,r-l+1)
print(maxl)