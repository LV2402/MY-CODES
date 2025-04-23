s=input()
h="hello"
k=0
for i in s:
    if k<5 and i==h[k]:
        k+=1
if k==5:
    print("YES")
else:
    print("NO")