def print_table(algorithm, sequence, frames, status, frames_count):
    print(f"\n{algorithm} Algorithm:")
    print("Sequence: ", end="")
    for num in sequence:
        print(num, end=" ")
    print()
    for i in range(frames_count):
        print(f"Frame {i + 1}:  ", end="")
        for frame in frames:
            print(frame[i], end=" ")
        print()
    print("Status:   ", end="")
    for c in status:
        print(c, end=" ")
    print()

def fifo(frames_count, sequence):
    frames = []
    status = [''] * len(sequence)
    frame_arr = [-1] * frames_count
    pointer = 0
    hits = 0
    faults = 0

    for j in range(len(sequence)):
        hit = False
        for frame in frame_arr:
            if frame == sequence[j]:
                hit = True
                break
        if hit:
            status[j] = 'H'
            hits += 1
        else:
            status[j] = 'F'
            frame_arr[pointer] = sequence[j]
            pointer = (pointer + 1) % frames_count
            faults += 1

        snapshot = []
        for frame in frame_arr:
            snapshot.append(" " if frame == -1 else str(frame))
        frames.append(snapshot)

    print_table("FIFO", sequence, frames, status, frames_count)
    print(f"Hits: {hits}, Faults: {faults}")

def optimal(frames_count, sequence):
    frames = []
    status = [''] * len(sequence)
    frame_list = []
    hits = 0
    faults = 0

    for j in range(len(sequence)):
        if sequence[j] in frame_list:
            status[j] = 'H'
            hits += 1
        else:
            status[j] = 'F'
            if len(frame_list) < frames_count:
                frame_list.append(sequence[j])
            else:
                farthest = -1
                replace_index = -1
                for i in range(len(frame_list)):
                    next_use = float('inf')
                    for k in range(j + 1, len(sequence)):
                        if sequence[k] == frame_list[i]:
                            next_use = k
                            break
                    if next_use > farthest:
                        farthest = next_use
                        replace_index = i
                frame_list[replace_index] = sequence[j]
            faults += 1

        snapshot = []
        for i in range(frames_count):
            snapshot.append(str(frame_list[i]) if i < len(frame_list) else " ")
        frames.append(snapshot)

    print_table("Optimal", sequence, frames, status, frames_count)
    print(f"Hits: {hits}, Faults: {faults}")

def lru(frames_count, sequence):
    frames = []
    status = [''] * len(sequence)
    frame_arr = [-1] * frames_count
    last_used = {}
    hits = 0
    faults = 0

    for j in range(len(sequence)):
        page = sequence[j]
        hit = False
        empty_index = -1
        for i in range(frames_count):
            if frame_arr[i] == page:
                hit = True
                status[j] = 'H'
                hits += 1
                break
            if frame_arr[i] == -1 and empty_index == -1:
                empty_index = i

        if not hit:
            status[j] = 'F'
            faults += 1
            if empty_index != -1:
                frame_arr[empty_index] = page
            else:
                lru_index = 0
                oldest = float('inf')
                for i in range(frames_count):
                    used_time = last_used.get(frame_arr[i], -1)
                    if used_time < oldest:
                        oldest = used_time
                        lru_index = i
                frame_arr[lru_index] = page

        last_used[page] = j

        snapshot = []
        for val in frame_arr:
            snapshot.append(" " if val == -1 else str(val))
        frames.append(snapshot)

    print_table("LRU", sequence, frames, status, frames_count)
    print(f"Hits: {hits}, Faults: {faults}")

# Taking input manually
frames_count = int(input("Enter number of frames: "))
n = int(input("Enter number of elements in sequence: "))
sequence = list(map(int, input("Enter sequence: ").split()))

fifo(frames_count, sequence)
optimal(frames_count, sequence)
lru(frames_count, sequence)