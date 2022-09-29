"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

import numbers
from modules import *

if __name__ == "__main__":
    MAX_COUNT = 10001

    prime_counts = 0
    target_prime = 0

    # search the prime number, and start from 2
    number = 2
    while True:
        # if the number is a prime number, we can add 1 to the prime_counts
        if is_prime(number) and prime_counts <= MAX_COUNT:
            target_prime = number
            prime_counts += 1

            if prime_counts % 100 == 0:
                print(f"the {prime_counts} prime is {target_prime}")
        
        # if the prime number is the MAX_COUNT, we can stop the search
        if prime_counts == MAX_COUNT:
            break

        # add 1 to the number
        number += 1
    
    print(f"the target {MAX_COUNT} prime is {target_prime}")