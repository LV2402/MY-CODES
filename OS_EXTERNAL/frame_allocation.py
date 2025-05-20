total_frames = int(input("Enter total number of frames in memory: "))
num_processes = int(input("Enter number of processes: "))

# List to store number of pages for each process
pages=[]
for i in range(num_processes):
    p= int(input(f"Enter number of pages for Process {i+1}: "))
    pages.append(p)

print("\n a) Minimum Number of Frames ")
for i in range(num_processes):
    print(f"Process {i+1}: Allocated {pages[i]} frames")

print("\n b) Equal Allocation")
equal = total_frames // num_processes
remainder = total_frames % num_processes
for i in range(num_processes):
    allocation = equal + (1 if i < remainder else 0)
    print(f"Process {i+1}: Allocated {allocation} frames")

print("\n c) Proportional Allocation")
total_pages = sum(pages)
for i in range(num_processes):
    proportion = int((pages[i] / total_pages) * total_frames)
    print(f"Process {i+1}: Allocated {proportion} frames proportionally")