import threading
import time
from queue import Queue

buffer = Queue(maxsize=5)  # Buffer size

# Semaphore to control access to the buffer
mutex = threading.Semaphore(1)

# Semaphore to signal when the buffer is not empty
full = threading.Semaphore(0)

# Semaphore to signal when the buffer is not full
empty = threading.Semaphore(buffer.maxsize)


def producer():
    for i in range(10):
        empty.acquire()  # Wait if the buffer is full
        mutex.acquire()  # Enter critical section
        item = f"Produced {i}"
        buffer.put(item)
        print(f"Produced: {item}")
        mutex.release()  # Exit critical section
        full.release()   # Signal that buffer is not empty
        time.sleep(1)


def consumer():
    for i in range(10):
        full.acquire()   # Wait if the buffer is empty
        mutex.acquire()  # Enter critical section
        item = buffer.get()
        print(f"Consumed: {item}")
        mutex.release()  # Exit critical section
        empty.release()  # Signal that buffer is not full
        time.sleep(1)


# Create producer and consumer threads
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

# Start threads
producer_thread.start()
consumer_thread.start()

# Wait for threads to finish
producer_thread.join()
consumer_thread.join()




# 2.) 
class BankerAlgorithm:
    def __init__(self, processes, resources):
        self.processes = processes
        self.resources = resources
        self.max_claim = [[5, 5, 7], [3, 2, 2], [9, 0, 2], [2, 2, 2], [4, 3, 3]]
        self.allocation = [[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]]
        self.need = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.safe_sequence = []
        self.work = resources.copy()
        self.finish = [False] * processes

    def calculate_need_matrix(self):
        for i in range(self.processes):
            for j in range(self.resources):
                self.need[i][j] = self.max_claim[i][j] - self.allocation[i][j]

    def is_safe_state(self):
        for i in range(self.processes):
            if not self.finish[i] and all(need <= self.work for need in self.need[i]):
                self.work = [work + allocation for work, allocation in zip(self.work, self.allocation[i])]
                self.safe_sequence.append(i)
                self.finish[i] = True
                return self.is_safe_state()

        return all(self.finish)

    def run(self):
        self.calculate_need_matrix()
        if self.is_safe_state():
            print("Safe state found.")
            print("Safe Sequence:", self.safe_sequence)
        else:
            print("Unsafe state. No safe sequence found.")


# Example usage:
banker = BankerAlgorithm(processes=5, resources=3)
banker.run()
