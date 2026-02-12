s="101100"
a,b=s.count("1"),s.count("0")
ns="1"*(a//2)+"0"*b+"1"*(a-a//2)
c=0
for i in range(len(s)):
    if s[i]!=ns[i]:
        c+=1
print(c//2)
print(ns)