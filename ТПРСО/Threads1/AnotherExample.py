import threading
import time
import random as r



class Program:
    def __init__(self):
        thread1 = threading.Thread(target = Program.func, args = [])
        thread2 = threading.Thread(target = Program.func, args = [])
        start = time.time()

        try:
            thread1.start()
            thread2.start()
            thread1.join()
            thread2.join()
            print(f'Multithread\nTime is {time.time() - start}\n')

        except:
            print("Ooops....")


    @classmethod
    def func(cls):
        for x in range(10):
            time.sleep(1 - (r.randint(0, 100)/100.))
            print(f'{threading.get_ident()}   {x}  ')        

Program()


start = time.time()
for x in range(10):
    time.sleep(1 - (r.randint(0, 100)/100.))
    print(f'{threading.get_ident()}   {x}  ')        

for x in range(10):
    time.sleep(1 - (r.randint(0, 100)/100.))
    print(f'{threading.get_ident()}   {x}  ')        
print(f'Linear\nTime is {time.time() - start}\n')