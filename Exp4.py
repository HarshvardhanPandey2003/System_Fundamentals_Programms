class OptimalCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = []

    def access_page(self, page):
        if page not in self.cache:
            if len(self.cache) < self.capacity:
                self.cache.append(page)
            else:
                farthest_page = max(
                    [(index, p) for index, p in enumerate(self.cache) if p not in pages[self.current_index:]],
                    key=lambda x: x[1]
                )[0]
                self.cache[farthest_page] = page

    def display_cache(self):
        print("Cache:", self.cache)


# Example usage
pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 1, 2, 0, 1, 7, 0, 1]
optimal_cache = OptimalCache(3)

for page in pages:
    optimal_cache.access_page(page)
    optimal_cache.display_cache()



from collections import deque

class FIFOCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = deque(maxlen=capacity)

    def access_page(self, page):
        if page not in self.cache:
            if len(self.cache) < self.capacity:
                self.cache.append(page)

    def display_cache(self):
        print("Cache:", list(self.cache))


# Example usage
fifo_cache = FIFOCache(3)

for page in pages:
    fifo_cache.access_page(page)
    fifo_cache.display_cache()




class FCFS:
    def __init__(self, processes):
        self.processes = processes

    def execute(self):
        for process in self.processes:
            print(f"Executing Process {process}")


# Example usage
processes_fcfs = [1, 2, 3, 4, 5]
fcfs_scheduler = FCFS(processes_fcfs)
fcfs_scheduler.execute()



class SJF:
    def __init__(self, processes):
        self.processes = processes

    def execute(self):
        self.processes.sort()
        for process in self.processes:
            print(f"Executing Process {process}")


# Example usage
processes_sjf = [5, 3, 1, 4, 2]
sjf_scheduler = SJF(processes_sjf)
sjf_scheduler.execute()



class PriorityNonPreemptive:
    def __init__(self, processes, priorities):
        self.processes = processes
        self.priorities = priorities

    def execute(self):
        sorted_processes = [x for _, x in sorted(zip(self.priorities, self.processes))]
        for process in sorted_processes:
            print(f"Executing Process {process}")


# Example usage
processes_priority = [1, 2, 3, 4, 5]
priorities = [3, 1, 4, 2, 5]
priority_scheduler = PriorityNonPreemptive(processes_priority, priorities)
priority_scheduler.execute()




class SRTF:
    def __init__(self, processes, burst_times):
        self.processes = processes
        self.burst_times = burst_times

    def execute(self):
        remaining_time = {process: burst for process, burst in zip(self.processes, self.burst_times)}
        current_time = 0

        while remaining_time:
            available_processes = {p: t for p, t in remaining_time.items() if t > 0 and current_time >= t}
            if not available_processes:
                current_time += 1
                continue

            shortest_process = min(available_processes, key=available_processes.get)
            print(f"Executing Process {shortest_process} at time {current_time}")
            remaining_time[shortest_process] -= 1
            if remaining_time[shortest_process] == 0:
                del remaining_time[shortest_process]

            current_time += 1

# Example usage
processes_srtf = ["P1", "P2", "P3", "P4", "P5"]
burst_times_srtf = [6, 8, 7, 3, 2]
srtf_scheduler = SRTF(processes_srtf, burst_times_srtf)
srtf_scheduler.execute()



from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def access_page(self, page):
        if page in self.cache:
            # Move the accessed page to the end
            self.cache.move_to_end(page)
        else:
            if len(self.cache) >= self.capacity:
                # Remove the least recently used page (first item in OrderedDict)
                self.cache.popitem(last=False)
            # Add the new page to the cache
            self.cache[page] = None

    def display_cache(self):
        print("LRU Cache:", list(self.cache.keys()))


# Example usage
pages_lru = [1, 2, 3, 1, 4, 5, 2, 3, 6]
lru_cache = LRUCache(3)

for page in pages_lru:
    lru_cache.access_page(page)
    lru_cache.display_cache()
