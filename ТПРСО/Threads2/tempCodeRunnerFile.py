
        lock = Lock()
        lock.acquire()
        try:
            self.arr.append(self.mass)
            self._mass += value
        finally:
            lock.release()