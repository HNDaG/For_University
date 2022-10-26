import threading
import time
from queue import Queue

Lock = threading.Lock()
result = list()  


def DasCollatzFunction(number: int):
        return int(number/2) if number % 2 == 0 else number*3+1


class CollatzNumberEvolution:
    def __init__(self, number):
        self.number = number
        self.current_change = number
        self.count = 1

    def __str__(self):
        return f"Number: {self.number} \t Steps: {self.count}"

    def dasCollatzProblem(self):
        self.current_change = DasCollatzFunction(self.current_change)
        self.count += 1


def MultiThreads(q):
    while not q.empty():
        Lock.acquire()
        try:
            Collatz = q.get()
        finally:
            Lock.release()
        
        Collatz.dasCollatzProblem()

        if Collatz.current_change != 1:
            Lock.acquire()
            try:
                q.put(Collatz)
            finally:
                Lock.release()
        else:
            result.append(Collatz)
            #print(result.__len__)
        
    
if __name__ == '__main__':
    threads_num =  int(input("Enter number of threads: "))
    number = int(input("Enter number for Collarz to calculate: "))
    q = Queue()

    for i in range(1, number+1):
        CollatzEvolution = CollatzNumberEvolution(i)
        q.put(CollatzEvolution)

    print("Done:\n Puttung into queue...")

    threads = list()
    start = time.time()

    for i in range(threads_num):
        threads.append(threading.Thread(target=MultiThreads, args=(q,)))
        threads[i].start()

    print("Done:\n Starting threads...")

    for i in range(threads_num):
        threads[i].join()
    end = time.time()
    print("Done:\n Waiting for threads...")


    for CollatzNum in result:
        print(CollatzNum)
    print(f"There is {threads_num} threads, calculating for {number} numbers took {end - start} seconds.")