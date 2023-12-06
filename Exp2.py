# 1.)
def round_robin(processes, burst_time, quantum):
    n = len(processes)
    remaining_time = burst_time.copy()
    waiting_time = [0] * n
    turnaround_time = [0] * n
    time = 0

    while True:
        done = True
        for i in range(n):
            if remaining_time[i] > 0:
                done = False
                if remaining_time[i] > quantum:
                    time += quantum
                    remaining_time[i] -= quantum
                else:
                    time += remaining_time[i]
                    waiting_time[i] = time - burst_time[i]
                    remaining_time[i] = 0
                    turnaround_time[i] = time

        if done:
            break

    print("Process\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(f"{processes[i]}\t{waiting_time[i]}\t\t{turnaround_time[i]}")

processes = [1, 2, 3]
burst_time = [10, 5, 8]
quantum = 2
round_robin(processes, burst_time, quantum)


# 2.)
def best_fit(block_size, process_size):
    m = len(block_size)
    n = len(process_size)
    allocation = [-1] * n

    for i in range(n):
        best_fit_idx = -1
        for j in range(m):
            if block_size[j] >= process_size[i]:
                if best_fit_idx == -1 or block_size[j] < block_size[best_fit_idx]:
                    best_fit_idx = j

        if best_fit_idx != -1:
            allocation[i] = best_fit_idx
            block_size[best_fit_idx] -= process_size[i]

    print("Process No.\tProcess Size\tBlock No.")
    for i in range(n):
        print(f"{i+1}\t\t{process_size[i]}\t\t{allocation[i]+1 if allocation[i] != -1 else 'Not Allocated'}")


# Example usage:
block_size = [100, 500, 200, 300, 600]
process_size = [212, 417, 112, 426]
best_fit(block_size, process_size)





# 3.)
def first_fit(memory_blocks, process_sizes):
    allocation = [-1] * len(process_sizes)

    for i in range(len(process_sizes)):
        for j in range(len(memory_blocks)):
            if memory_blocks[j] >= process_sizes[i]:
                allocation[i] = j
                memory_blocks[j] -= process_sizes[i]
                break

    print("Process No.\tProcess Size\tBlock No.")
    for i in range(len(process_sizes)):
        print(f"{i + 1}\t\t{process_sizes[i]}\t\t", end="")
        if allocation[i] != -1:
            print(allocation[i] + 1)
        else:
            print("Not Allocated")


# Example usage:
memory_blocks = [100, 500, 200, 300, 600]
process_sizes = [212, 417, 112, 426]
first_fit(memory_blocks, process_sizes)




# 4.)
def worst_fit(memory_blocks, process_sizes):
    allocation = [-1] * len(process_sizes)

    for i in range(len(process_sizes)):
        worst_index = -1
        for j in range(len(memory_blocks)):
            if memory_blocks[j] >= process_sizes[i]:
                if worst_index == -1 or memory_blocks[j] > memory_blocks[worst_index]:
                    worst_index = j

        if worst_index != -1:
            allocation[i] = worst_index
            memory_blocks[worst_index] -= process_sizes[i]

    print("Process No.\tProcess Size\tBlock No.")
    for i in range(len(process_sizes)):
        print(f"{i + 1}\t\t{process_sizes[i]}\t\t", end="")
        if allocation[i] != -1:
            print(allocation[i] + 1)
        else:
            print("Not Allocated")


# Example usage:
memory_blocks = [100, 500, 200, 300, 600]
process_sizes = [212, 417, 112, 426]
worst_fit(memory_blocks, process_sizes)






