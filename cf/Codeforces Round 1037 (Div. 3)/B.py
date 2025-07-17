for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))

    hikes=0
    i=0
    while i<=n-k:  
        can_hike=True
        for j in range(k):
            if a[i+j]==1:  
                can_hike=False
                i=i+j+1  
                break
        
        if can_hike:
            hikes+=1
            i=i+k+1  
        
    print(hikes)