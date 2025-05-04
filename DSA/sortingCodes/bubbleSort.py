def bubble_sort(arr):
    n = len(arr)
    for i in range(n):  # Do this n times
        for j in range(0, n - i - 1):  # Each time go a bit less far
            if arr[j] > arr[j + 1]:  # If the left number is bigger
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap!
        print(arr)  # Print after each pass
    return arr  # Return the sorted array

# Try it out
numbers = [5, 3, 8, 4, 2]
sorted_numbers = bubble_sort(numbers)