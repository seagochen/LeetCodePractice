"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

def findTriplet(sum=1000):
    # search a, b, c from the last to the first
    for c in range(sum-3, 1, -1):
        for b in range(c-1, 1, -1):
            for a in range(b-1, 1, -1):
                if a + b + c == sum and a**2 + b**2 == c**2:
                    return a, b, c, a*b*c

def main():
    print(findTriplet())

if __name__ == "__main__":
    main()