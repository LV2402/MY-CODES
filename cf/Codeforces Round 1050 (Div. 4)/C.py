for _ in range(int(input())):
    n,m=map(int,input().split())
    req=[]
    for _ in range(n):
        a,b=map(int,input().split())
        req.append((a,b))
    
    pos=0
    points=0
    last=0
    for a,b in req:
        dist=a-last
        points+=dist
        if (pos+dist)%2!=b: 
            points-=1
        pos=b
        last=a
    points+=m-last  
    print(points)
