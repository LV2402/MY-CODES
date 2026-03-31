l=list(map(int,input().split()))
j=-1
for i in range(len(l)):
    if l[i]==0:
        j=i
        break

for i in range(j+1,len(l)):
    if l[i]!=0:
        l[i],l[j]=l[j],l[i]
        j+=1
print(l)