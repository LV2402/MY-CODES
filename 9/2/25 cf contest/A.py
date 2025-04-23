for _ in range(int(input())):
    s=input()
    if s.count("us")>1:
        s=s[:-2]+"i"
    else:
        s=s.replace("us","i")
    print(s)