n=int(input())
m=[]
c=0
for _ in range(n):
    row=list(map(int,input().split()))
    a=row.count(1)
    if a>=2:
        c+=1
    m.append(row)
print(c)