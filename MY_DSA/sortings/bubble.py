def bubbleSort(l,n):
    if n==1:
        return
    did_swap=True
    for j  in range(n-1):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
    if not did_swap:
        return
    bubbleSort(l,n-1)


l=list(map(int,input().split()))
n=len(l)
bubbleSort(l,n)
print(l)
# for i in range(len(l)-1,0,-1):
#     didS=0
#     for j in range(i):
#         if l[j]>l[j+1]:
#             l[j],l[j+1]=l[j+1],l[j]
#             didS=1
#     if didS==0:break
#     print(l)

