import sys
import time
import math
from heapq import *

class maxHeap():
    def __init__(self):
        self.t = []
        self.size = 0

    def insert(self, x):
        self.size += 1
        heappush(self.t, -1*x)

    def pop(self):
        self.size -= 1
        return -1*heappop(self.t)

class minHeap():
    def __init__(self):
        self.t = []
        self.size = 0

    def insert(self, x):
        self.size += 1
        heappush(self.t, x)

    def pop(self):
        self.size -= 1
        return heappop(self.t)

def driver():
    lower = maxHeap()
    upper = minHeap()
    pivot = None
    final = ""

    with open(sys.argv[1]) as f:
        n = int(f.readline().strip())

        for _ in range(n):
            current = int(f.readline().strip())

            #This section assigns the current value to a heap
            if pivot == None:
                pivot = current
                lower.insert(pivot)
            else:
                if current <= pivot:
                    lower.insert(current)
                else:
                    upper.insert(current)

            #Rebalances the sizes of the heaps
            while abs(upper.size - lower.size) > 1:
                if upper.size > lower.size:
                    t1 = upper.pop()
                    lower.insert(t1)
                else:
                    t1 = lower.pop()
                    upper.insert(t1)

            #This section determines the median by comparing the sizes of the heaps
            if upper.size - lower.size != 0: #NOTE TO SELF, NEED TO ENSURE DIFF SIZE DOES NOT EXCEED 1
                if upper.size > lower.size:
                    pivot = upper.pop()
                    final += str(pivot) + "\n"
                    upper.insert(pivot)
                else:
                    pivot = lower.pop()
                    final += str(pivot) + "\n"
                    lower.insert(pivot)
            else:
                t1, t2 = upper.pop(), lower.pop()
                pivot = (t1 + t2) / 2
                upper.insert(t1)
                lower.insert(t2)
                if pivot - int(pivot) == 0:
                    pivot = int(pivot)
                final += str(pivot) + "\n"
        print(final)

start_time = time.time()
driver()
print("--- %s seconds ---" % (time.time() - start_time))