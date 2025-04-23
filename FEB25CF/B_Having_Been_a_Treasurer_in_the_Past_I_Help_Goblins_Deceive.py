for _ in range(int(input())):
    n=int(input())
    s=input()
    dc=s.count("-")
    uc=s.count("_")
    x=dc//2
    y=dc-x
    ans=uc*(x*y)
    if uc==0 or dc<2:
        print("0")
    else:
        print(ans)
