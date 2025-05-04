def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i  # Assume current is the smallest
        for j in range(i+1, n):  # Check the rest
            if arr[j] < arr[min_index]:
                min_index = j  # Found smaller one
        # Swap smallest with current position
        arr[i], arr[min_index] = arr[min_index], arr[i]
        print(arr)
    return arr


# Try it
numbers = [64, 25, 12, 22, 11]
sorted_numbers = selection_sort(numbers)
print(sorted_numbers)
# Output: [11, 12, 22, 25, 64]