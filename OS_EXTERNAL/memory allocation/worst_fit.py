def best_fit(block_sizes, m, process_sizes, n):
    # Create a list of (block_size, original_index)
    blocks = sorted([(block_sizes[i], i) for i in range(m)],reverse=True)
    
    allocation = [-1] * n
    used = [False] * m  # To track which blocks are already allocated

    for i in range(n):
        for size, idx in blocks:
            if size >= process_sizes[i] and not used[idx]:
                allocation[i] = idx
                used[idx] = True
                break

    print("Process No.\tProcess Size\tBlock No.")
    for i in range(n):
        if allocation[i] != -1:
            print(f"P{i + 1}\t\t{process_sizes[i]}\t\tB{allocation[i] + 1}")
        else:
            print(f"P{i + 1}\t\t{process_sizes[i]}\t\tNot Allocated")

# Input
m = int(input("Enter the number of blocks: "))
block_sizes = list(map(int, input("Enter the block sizes: ").split()))
n = int(input("Enter the number of processes: "))
process_sizes = list(map(int, input("Enter the process sizes: ").split()))

best_fit(block_sizes, m, process_sizes, n)