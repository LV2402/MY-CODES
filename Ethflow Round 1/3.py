def diff(a):
    n = len(a)
    l = []
    for i in range(n - 1):
        l.append(a[i + 1] - a[i])
    return l

def ans(arr):
    while len(arr) > 1:
        # Calculate the maximum sum of the array
        max_sum = sum(arr)
        # Reverse the array and calculate its difference sequence
        arr.reverse()
        arr = diff(arr)
        # If the current max_sum is greater, break early
        if max_sum >= sum(arr):
            return max_sum
    return arr[0]

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    print(ans(arr))
