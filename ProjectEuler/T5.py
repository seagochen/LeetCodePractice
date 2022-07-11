"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
import math


def is_prime(n):
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


def pick_prime_numbers(start=1, end=100):
    prime_list = []
    for i in range(start, end + 1):
        if is_prime(i):
            prime_list.append(i)

    return prime_list


def find_out_prime_factors(number: int):
    # first, we list some prime numbers below 1000
    start = 2
    end = 1000
    constant = number
    prime_numbers = pick_prime_numbers(start=start, end=end)

    # an empty list is preparing to store the correct prime numbers
    result = []

    while True:
        if len(prime_numbers) > 0:
            prime = prime_numbers.pop(0)

            # the number should be divisible by some prime numbers
            if number % prime == 0:
                result.append(prime)
                number = int(number / prime)

        elif len(prime_numbers) == 0 and number > 1:
            if end + 1000 < constant:
                start = end
                end = end + 1000
                prime_numbers = pick_prime_numbers(start=start, end=end)

            else:
                break
        else:
            break

    return result


if __name__ == "__main__":
    print(find_out_prime_factors(600851475143))
