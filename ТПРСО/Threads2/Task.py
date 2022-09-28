from threading import *
import random as r
import time


class Rise:
    arr = []
    def __init__(self, value = 0.0):
        self._mass = value

    @property
    def mass(self):
        return self._mass

    @mass.setter
    def mass(self, value):
        self._mass = value

class Potatoes:
    arr = []
    def __init__(self, value = 0.0):
        self._mass = value

    @property
    def mass(self):
        return self._mass

    @mass.setter
    def mass(self, value):
        self._mass = value


def adder(cl, value):
    for i in range(value):
        to_add = r.random()
        try:
            lock = Lock()
            lock.acquire()
            cl.arr.append(cl.mass)
            cl.mass += to_add
        finally:
            lock.release()


if __name__ == '__main__':
    R = Rise()
    P = Potatoes()

    start = time.time()
    threads = []
    N = r.randint(10, 30)
    for n in range(N):
        if n < N / 2:
            t = Thread(target=adder, args=(P, r.randint(10000, 20000)))
            threads.append(t)
            threads[-1].start()
        else:
            t = Thread(target=adder, args=(R, r.randint(10000, 20000)))
            threads.append(t)
            threads[-1].start()

    for thread in threads:
        thread.join()


    print(f"Answer is {(R.mass, P.mass)}")
    print(f"Time is {time.time() - start}")
    # check is it accurate
    '''
    for i in range(len(R.arr)-1):
        if R.arr[i] in R.arr[i+1:]:
            print("error")

    for i in range(len(P.arr)-1):
        if P.arr[i] in P.arr[i+1:]:
            print("error")
    print("Ok")
    '''

