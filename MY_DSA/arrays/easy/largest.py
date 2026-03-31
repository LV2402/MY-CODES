l=list(map(int,input().split()))
m=float("-inf")
for i in range(len(l)):
    if l[i]>m:
        m=l[i]
print(m)