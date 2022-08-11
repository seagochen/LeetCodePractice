# import standard input/output library
import sys

def solution():
    # write your code in Python 3.6
    N = int(input())
    for i in range(N):
        X = int(input())
        Yn = [int(i) for i in input().split()]
        sum = 0
        for j in Yn:
            if j > 0:
                sum += j**2
        print(sum)

if __name__ == '__main__':
    # read input from standard input
    input = sys.stdin.readline
    print(input)