"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

from functools import reduce


def is_palindromic(num: int):
    # convert number to string
    str_num = str(num)
    length = int(len(str_num) / 2)
    is_odd = len(str_num) % 2

    # split the converted string into two sets
    if is_odd == 1:  # if odd
        sp1 = str_num[0: length+1]
        sp2 = str_num[length: len(str_num)]

    else:  # if even
        sp1 = str_num[0: length]
        sp2 = str_num[length: len(str_num)]

    # swap sp2
    sp2 = reduce(lambda x, y: y + x, sp2)

    # is sp1 equivalent sp2
    return sp1 == sp2


def largest_palindrome_digits(max_num: int, min_num):

    max = 0
    m_i = m_j = 0

    for i in range(max_num, min_num, -1):
        for j in range(i, min_num, -1):
            if is_palindromic(i * j):
                result = i * j
                if result > max:
                    max = result
                    m_i = i
                    m_j = j

    return max, m_i, m_j

if __name__ == "__main__":
    print(largest_palindrome_digits(999, 100))
