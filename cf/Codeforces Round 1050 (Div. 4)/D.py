for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    evens=[x for x in a if x%2==0]
    odds=[x for x in a if x%2==1]
    if not odds:
        print(0)
        continue
    evens_sum=sum(evens)
    odds.sort(reverse=True)
    take=(len(odds)+1)//2
    odds_sum=sum(odds[:take])
    print(evens_sum+odds_sum)