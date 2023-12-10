import threading
from queue import Queue
import time 

buffer = Queue(maxsize=5)

mutex = threading.Semaphore(1)
empty = threading.Semaphore(buffer.maxsize)
full = threading.Semaphore(0)

def Producer():
    for i in range(10):
        empty.acquire()#Waits if the Queue is not Full
        mutex.acquire()
        item=f"Produced : {i}"
        buffer.put(item)
        print(f"Produced : {item}")
        mutex.release()
        full.release()# Sends a alaert that queue is not empty
        time.sleep(1)

def Consumer():
    for i in range(10):
        full.acquire()#Waits to see if the Queue is not empty 
        mutex.acquire()
        buffer.get()
        print(f"Consumed : {i}")
        mutex.release()
        empty.release()
        time.sleep(1)

Producer_thread = threading.Thread(target = Producer)
Consumer_thread = threading.Thread(target = Consumer)

Producer_thread.start()
Consumer_thread.start()

#Waiting for the threads to finish 
Producer_thread.join()
Consumer_thread.join()