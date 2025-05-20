# Input: Page size, number of pages, number of frames, number of logical addresses
page_size, num_pages, num_frames, num_addresses = map(int, input("Enter Page Size, Number of Pages, Number of Frames, Number of Addresses: ").split())

# Input: Logical addresses
print("Enter the logical addresses (space-separated):")
logical_addresses = list(map(int, input().split()))

# Simulate a simple page table using modulus mapping
# (for each page number, assign it to a frame number)
page_table = {page_number: page_number % num_frames for page_number in range(num_pages)}

# Output: Page Table
print("\nPage Table (Page -> Frame):")
for page_number, frame_number in page_table.items():
    print(f"Page {page_number} -> Frame {frame_number}")

# Translate each logical address to a physical address
print("\nAddress Translation (Logical -> Physical):")
for logical_address in logical_addresses:
    page_number, offset = divmod(logical_address, page_size)

    # If page number is invalid (exceeds the defined pages), mark as invalid
    if page_number >= num_pages:
        print(f"Logical Address {logical_address} is INVALID (page {page_number} not defined)")
        continue

    # Physical address = (frame number * page size) + offset
    frame_number = page_table[page_number]
    physical_address = frame_number * page_size + offset
    print(f"Logical Address {logical_address} => Physical Address {physical_address}")