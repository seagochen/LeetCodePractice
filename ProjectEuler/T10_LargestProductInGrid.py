"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from modules import find_primes

def main():

    fragments = 2_000_000 / 1_000

    # sum the primes respectively
    sum_primes = 0
    for i in range(1000):
        start = int(i * fragments)
        end = int((i + 1) * fragments)
        sum_primes += sum(find_primes(start, end))

        # debug message
        print(f"Sum of primes from {start} to {end} is {sum_primes}")


if __name__ == "__main__":
    main()