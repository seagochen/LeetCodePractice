"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""


def find_multiples(limitation: int, multiples: int):
    elements = []
    sum = 0
    times = int(limitation / multiples)

    if times * multiples == limitation:
        times = times - 1

    for i in range(1, times + 1):
        elements.append(i * multiples)
        sum += i*multiples

    return sum, elements


if __name__ == "__main__":

    a, list_a = find_multiples(limitation=1000, multiples=3)
    b, list_b = find_multiples(limitation=1000, multiples=5)
    c, list_c = find_multiples(limitation=1000, multiples=15)

    print(a + b - c)
