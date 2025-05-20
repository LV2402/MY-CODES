from collections import deque

def round_robin():
    n = int(input("Enter the number of processes: "))
    tq = int(input("Enter the time quantum: "))
    
    print("Enter Process ID, Arrival Time, and Burst Time:")
    processes = []
    for _ in range(n):
        pid, at, bt = input().split()
        processes.append([pid, int(at), int(bt), int(bt), 0, 0])  # pid, at, bt, remaining_bt, ct, tat

    processes.sort(key=lambda x: x[1])  # Sort by Arrival Time
    ready_queue = deque()
    gc = []  # Gantt Chart
    time_stamps = []
    current_time = 0
    completed = 0
    index = 0

    while completed < n:
        while index < n and processes[index][1] <= current_time:
            ready_queue.append(processes[index])
            index += 1

        if ready_queue:
            p = ready_queue.popleft()
            gc.append(p[0])
            time_stamps.append(current_time)

            run_time = min(tq, p[3])
            current_time += run_time
            p[3] -= run_time

            while index < n and processes[index][1] <= current_time:
                ready_queue.append(processes[index])
                index += 1

            if p[3] > 0:
                ready_queue.append(p)
            else:
                p[4] = current_time  # CT
                p[5] = p[4] - p[1]   # TAT
                completed += 1
        else:
            gc.append("Idle")
            time_stamps.append(current_time)
            current_time += 1

    time_stamps.append(current_time)

    total_wt = 0
    total_tat = 0
    print("\nPID\tAT\tBT\tCT\tTAT\tWT")
    for p in processes:
        wt = p[5] - p[2]
        total_tat += p[5]
        total_wt += wt
        print(f"{p[0]}\t{p[1]}\t{p[2]}\t{p[4]}\t{p[5]}\t{wt}")

    print("\nGantt Chart:")
    for pid in gc:
        print(f"| {pid} ", end="")
    print("|")
    for t in time_stamps:
        print(f"{t}\t", end="")
    print()

    print(f"\nAverage Turnaround Time (TAT): {total_tat / n:.2f}")
    print(f"Average Waiting Time (WT): {total_wt / n:.2f}")

round_robin()