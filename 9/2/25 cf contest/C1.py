for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = int(input())

    # Apply the operation if it helps to sort the sequence
    for i in range(n):
        if i > 0 and a[i] < a[i - 1]:
            a[i] = b - a[i]

    # Check for non-decreasing and non-increasing order
    is_non_decreasing = all(a[i] <= a[i + 1] for i in range(n - 1))
    is_non_increasing = all(a[i] >= a[i + 1] for i in range(n - 1))

    if is_non_decreasing or is_non_increasing:
        print("YES")
    else:
        print("NO")
