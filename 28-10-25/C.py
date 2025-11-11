for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    o,e=0,0
    for i in l:
        if i%2==0:
            e+=1
        else:
            o+=1
    if o>=1 and e>=1:
        l.sort()
    print(*l)