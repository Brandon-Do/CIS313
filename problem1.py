import sys
import time
from queue import *

class PQueue(PriorityQueue):
#Reference to Code: https://stackoverflow.com/questions/9289614/how-to-put-items-into-priority-queues
    def __init__(self):
        PriorityQueue.__init__(self)

    def put(self, ip, priorityNum):
        PriorityQueue.put(self, (priorityNum, ip))

    def get(self, *args, **kwargs):
        priorityNum, ip = PriorityQueue.get(self, *args, **kwargs)
        return ip

def driver():
    pqA = PQueue()
    pqB = PQueue()
    with open(sys.argv[1]) as f:
        n = int(f.readline().strip())
        for _ in range(n):
            ip, priorityClass, priorityNum = f.readline().strip().split()
            if priorityClass == 'A':
                pqA.put(ip, int(priorityNum))
            else:
                pqB.put(ip, int(priorityNum))

    while not (pqA.empty() and pqB.empty()):
        if not pqA.empty():
            print(pqA.get())
            #print("PQA Prints:{}".format(pqA.get()))
        else:
            print(pqB.get())
            #print("PQB Prints:{}".format(pqB.get()))


start_time = time.time()
driver()
print("--- %s seconds ---" % (time.time() - start_time))