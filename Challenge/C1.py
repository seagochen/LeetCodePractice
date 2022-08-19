# import standard IO library
from sys import stdin, stdout

def load_input_from_std(inputs: dict, cases: int = 0, numbs: int = 0):
    # if cases == -2:  # first line will be read as number of cases
    #     cases = int(stdin.readline())
    #     if cases < 0:
    #         raise ValueError("Number of cases must be positive")
    #     else:
    #         return load_input_from_std(inputs, cases, numbs)
    
    # elif cases >= 0:  # number of cases will be processed
    #     if numbs == -2:  # second line will be read as number of numbers
    #         numbs = int(stdin.readline())
    #         if numbs < 0:
    #             raise ValueError("Number of values must be greater than 0")
    #         else:
    #             return load_input_from_std(inputs, cases, numbs)
    #     elif numbs >= 0:

    return inputs


def main():
    inputs = {}

    # load input from stdin
    processed = load_input_from_std(inputs)


if __name__ == "__main__":
    main()