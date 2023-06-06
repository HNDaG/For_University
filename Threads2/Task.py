from threading import *
import random as r
import time


class Rice:
    arr = list()
    def __init__(self, value = 0.0):
        self._mass = value

    @property
    def mass(self):
        lock = Lock()
        lock.acquire()
        try:
            value = self._mass
        finally:
            lock.release()
            return value

  
    def set_mass(self, value):

        lock = Lock()
        lock.acquire()
        try:
            self.arr.append(self.mass)
            self._mass += value
        finally:
            lock.release()


    
    

class Potatoes:
    arr = list()
    def __init__(self, value = 0.0):
        self._mass = value

    @property
    def mass(self):
        lock = Lock()
        lock.acquire()
        try:
            value = self._mass
        finally:
            lock.release()
            return value

  
    def set_mass(self, value):
        lock = Lock()
        lock.acquire()
        try:
            self.arr.append(self.mass)
            self._mass += value
        finally:
            lock.release()

    
def adder(cl, value):
    for i in range(value):
        to_add = r.random()
        cl.set_mass(to_add )
            
    
if __name__ == '__main__':
    R = Rice()
    P = Potatoes()

    le = 10000
    ri = 20000

    rnd1 = r.randint(le, ri)
    rnd2 = r.randint(le, ri)

    start = time.time()
    threads = []
    N = r.randint(10, 30)


    for n in range(N):
        if n < N / 2:
            t = Thread(target=adder, args=(P, rnd1))
            threads.append(t)
            threads[-1].start()
        else:
            t = Thread(target=adder, args=(R, rnd2))
            threads.append(t)
            threads[-1].start()


    for thread in threads:
        thread.join()


    print(f"Answer is {(R.mass, P.mass)}")
    print(f"Time is {time.time() - start}")

    
    # check is it accurate
    if len(R.arr) == len(set(R.arr)):
        print("Error, there is some dublicates...")
    print("Rice is done...")
    if len(P.arr) == len(set(P.arr)):
        print("Error, there is some dublicates...")
    print("Potatoes is done...")
    

