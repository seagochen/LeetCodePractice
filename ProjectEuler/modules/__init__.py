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