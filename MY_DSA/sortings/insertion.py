def insertion_sort(arr, i, n):
    # Base case
    if i == n:
        return

    j = i
    # Move the element to the left while it's smaller than its predecessor
    while j > 0 and arr[j - 1] > arr[j]:
        # Swap
        arr[j - 1], arr[j] = arr[j], arr[j - 1]
        j -= 1

    # Recur for the next index
    insertion_sort(arr, i + 1, n)

l=list(map(int,input().split()))


print("Before Using Insertion Sort:")
print(l)

insertion_sort(l, 0, len(l)-1)

print("After Using Insertion Sort:")
insertion_sort(l,0,len(l))
print(l)
# for i in range(1,len(l)):
#     j=i
#     while j>0 and l[j-1]>l[j]:
#         l[j],l[j-1]=l[j-1],l[j]
#         j-=1
#     print(l)