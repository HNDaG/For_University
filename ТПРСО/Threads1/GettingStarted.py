from concurrent.futures import thread
import threading
import time
from LinearImplementation import ProgramLin, end1, end2


class Program:
    results = []
    def __init__(self):
        thread1 = threading.Thread(target = Program.func, args = [end1])
        thread2 = threading.Thread(target = Program.func, args = [end2])
        start = time.time()

        try:
            thread1.start()
            thread2.start()
            thread1.join()
            thread2.join()
            print(f'Multithread\nTime is {time.time() - start}\nAnswer is {Program.results[0] + Program.results[1]}\n\n\n')

        except:
            print("Ooops....")


    @classmethod
    def func(cls, right):
        start = time.time()
        ans = 0
        for x in range(right+1):
            ans+=x
        cls.results.append(ans)
        print(f'{threading.get_ident()} Time is {time.time() - start}')

        

Program()
ProgramLin() # Is the same as Program(), but implemented linearly
