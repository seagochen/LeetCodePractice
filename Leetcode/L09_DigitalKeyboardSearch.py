from typing import List

def solution(digits: str, num: str) -> int:
    # convert string of num to list of int
    num = [int(x) for x in num]

    # Calculate the time needed to type the number
    time = 0

    # convert arr to a dict for faster lookup
    # from [2, 4, 5, 10] to {2: 0, 4: 1, 5: 2, 10: 3}
    index = {int(x): i for i, x in enumerate(digits)}

    # iterate the list of num
    for i in range(len(num)):
        # if it's the first number, no need to calculate the time
        if i == 0:
            time += index[num[i]]
        else:
            # calculate the time needed to type the number
            # by finding the difference between the current number and the previous number
            time += abs(index[num[i]] - index[num[i - 1]])
    
    return time


def main():
    digits = "8459761203"
    num = "5439"
    print(solution(digits, num))

if __name__ == "__main__":
    main()