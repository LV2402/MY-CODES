for _ in range(int(input())):
    s = list(input())  
    f=0
    for i in range(1,len(s)):
        if s[i]==s[i-1]:
            f=1
            break
    if f==0:
        print(len(s))
    else:
        print("1")