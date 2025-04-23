s,n=map(int,input().split())
l=[]
f=0
for i in range(n):
    x,y=map(int,input().split())
    l.append((x,y))
l.sort(key=lambda x: x[0])
for x,y in l:
    if s>x:
        s+=y
    else:
        f=1
        break

if f==0:
    print("YES")
else:
    print("NO")