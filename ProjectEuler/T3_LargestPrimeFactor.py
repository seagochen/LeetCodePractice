"""
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + 3^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + 3 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .
3025 - 385 = 2640
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""


def cal_sum_of_the_squares(limitation: int):
    sum = 0
    for i in range(1, limitation + 1):
        sum += i ** 2

    return sum


def cal_square_of_the_sum(limitation: int):
    sum = limitation * (limitation + 1) / 2
    sum = int(sum)
    return sum * sum


if __name__ == "__main__":
    sum_sqr = cal_sum_of_the_squares(100)
    sqr_sum = cal_square_of_the_sum(100)

    print(sqr_sum - sum_sqr)
