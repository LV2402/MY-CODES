for _ in range(int(input())):
    n=int(input())
    l=list(str(n))
    # print(n,l,nl)
    if len(l)==1:
        print(int(l[0]))
    else:
        print(min(map(int,l)))