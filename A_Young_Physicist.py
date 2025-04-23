n=int(input())
sx,sy,sz=0,0,0
for _ in range(n):
    l=list(map(int,input().split()))
    sx+=l[0]
    sy+=l[1]
    sz+=l[2]
if sx==0 and sy==0 and sz==0 :
    print("YES")
else:
    print("NO")