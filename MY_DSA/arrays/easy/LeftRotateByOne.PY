l=list(map(int,input().split()))
t=l[0]
for i in range(1,len(l)):
    l[i-1]=l[i]
l[len(l)-1]=t
print(l)