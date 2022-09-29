import threading


def is_prime(n: int):
    """
    If a number is not a prime, one of its remainders is definitely in the left half.
    """
    if n < 1:
        return False

    half = int(n / 2)

    if half == 0 or half == 1:
        return True

    for i in range(2, half + 1):
        if n % i == 0:  # 6 % 2 == 0
            return False

    return True


class SearchPrimesThread(threading.Thread):
   def __init__(self, start, end):
       # Call the Thread class's init function
       threading.Thread.__init__(self)
       self.start_pos = start   # to avoid use the name "start" in the function
       self.end_pos = end       

   def run(self):
        self.result = [i for i in range(self.start_pos, self.end_pos) if is_prime(i)]


def find_primes(start=2, end=100, thread=1):
    """
    Find all primes below n.
    """
    if thread == 1:
        return [i for i in range(start, end) if is_prime(i)]
    else:
        threads = []
        for i in range(thread):
            # calculate the start and end position for each thread
            start_pos = int(i * end / thread)
            end_pos = int((i + 1) * end / thread)

            t = SearchPrimesThread(start_pos, end_pos)
            t.start()
            threads.append(t)
        
        for t in threads:
            t.join()

        return [i for t in threads for i in t.result]