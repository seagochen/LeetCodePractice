"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""


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


def pick_prime_numbers(limitation: int):
    prime_list = []
    for i in range(1, limitation + 1):
        if is_prime(i):
            prime_list.append(i)

    return prime_list


def find_the_minimum_number(limitation: int):
    prime_list = pick_prime_numbers(limitation)
    minimum_multiple = 1

    # multiply all prime numbers together
    for i in prime_list:
        minimum_multiple = minimum_multiple * i

    # use the number below the limitation to divide the minimum multiple,
    # so that we can find out if the minimum number is not divisible by which number
    for i in range(2, limitation + 1):
        if minimum_multiple % i != 0:
            for j in range(1, i + 1):
                temp_number = minimum_multiple * j
                if temp_number % i == 0:
                    minimum_multiple = temp_number
                    break

    return minimum_multiple


if __name__ == "__main__":
    print(find_the_minimum_number(20))
