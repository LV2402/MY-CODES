def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  # Current element to insert
        j = i - 1
        # Move elements of arr[0..i-1] that are > key to one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # Shift right
            j -= 1
        arr[j + 1] = key  # Insert in correct spot
    return arr

# Try it
numbers = [5, 3, 4, 1, 2]
print(insertion_sort(numbers))
