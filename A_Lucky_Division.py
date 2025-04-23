n=input()
f=1
for i in n:
    if i not in "47" and int(n)%4!=0 and int(n)%7!=0 :
        f=0
if f==0:
    print("NO")
else:
    print("YES")