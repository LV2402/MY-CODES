def reverse(l,s,e):
    while s<=e:
        l[s],l[e]=l[e],l[s]
        s+=1
        e-=1

l=list(map(int,input().split()))
k=int(input())
n=len(l)
reverse(l,0,k-1)
reverse(l,k,n-1)
reverse(l,0,n-1)
print(l)
# for i in range(k,n):
#     print(l[i],end=" ")
# for i in range(k):
#     print(l[i],end=" ")
