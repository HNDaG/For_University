from concurrent.futures import thread
import threading
import time

end1 = 10000000
end2 = 20000000

class ProgramLin:
    results = []
    def __init__(self):
    
        start = time.time()
        ProgramLin.func(end1)

        print(f"First part is done...\n Time {time.time() - start}")
        start2 = time.time()
        ProgramLin.func(end2)
        print(f"Second part is done...\n Time {time.time() - start2}")
        print(f'Linear\nTime is {time.time() - start}\nAnswer is {ProgramLin.results[0] + ProgramLin.results[1]}\n')
    

    @classmethod
    def func(cls, right):
        ans = 0
        for x in range(right+1):
            ans+=x
        cls.results.append(ans)
        

