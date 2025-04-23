vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U","Y","y"]
s=input()
for i in s:
    if i in vowels:
        s=s.replace(i,"")
s=list(s)
for i in range(len(s)):
    s[i]="."+s[i]
s="".join(s)
print(s.lower())