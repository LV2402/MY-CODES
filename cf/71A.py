for _ in range(int(input())):
    s=input()
    if len(s)<=10:
        print(s)
    else:
        print(s[0]+str(len(s)-2)+s[len(s)-1])