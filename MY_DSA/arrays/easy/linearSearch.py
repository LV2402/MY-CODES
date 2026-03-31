l=list(map(int,input().split()))
k=int(input())
n=len(l)
found=False
for i in range(n):
    if l[i]==k:
        found=True
        t=i
        break
if not found:
    print(-1)
else:print(t)