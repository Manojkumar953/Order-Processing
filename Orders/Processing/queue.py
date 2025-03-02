from collections import deque
from .worker import worker

# FIFO queue to store the events
queue = deque()

# scans the queue and if the queue has events then calls the worker method
def scan_queue():
    while queue:
        worker(queue.pop())

# add event into the queue
def add_task(event):
    queue.append(event)
