# import standard IO library
from sys import stdin, stdout


def convert_to_int_list(str_list: list, int_list: list):
    if len(str_list) == 0:
        return int_list

    # pop out the first element of the list
    number = prevent_error_int(str_list.pop(0))
    int_list.append(number)

    return convert_to_int_list(str_list, int_list)


def prevent_error_int(str_input):
    try:
        return int(str_input)
    except ValueError:
        return 0


def read_input_from_std(inputs: list, lines: int, cases: int = 0):
    if lines == 0:
        return inputs

    # read the next line and decrease the number of lines by 1
    input = stdin.readline()
    lines -= 1

    # if cases > 0, then we are reading the input for a case
    if cases > 0:
        # split the input into a list of integers by space
        input = input.split(" ")

        # convert the input to integers
        input = convert_to_int_list(input, [])

        # we will trim or pad the input to the length of cases
        input = input[:cases] + [0] * (cases - len(input))

        # append the input to the list of inputs
        inputs.append(input)

    # if current number of line is odd, then next input is cases
    cases = prevent_error_int(input) if lines % 2 == 1 else 0
    return read_input_from_std(inputs, lines, cases)


def sum_pos(input: list, sum: int = 0):
    if len(input) == 0:
        return sum

    # pop out the first element of the input
    number = input.pop(0)

    # if the number is positive, then append it to the output
    if number > 0:
        sum += number**2

    return sum_pos(input, sum)


def sum_of_positive_integers(input: list, output: list):
    if len(input) == 0:
        return output
    
    # pop out the first element of the input
    case = input.pop(0)

    # create a list of positive integers from the case
    result = sum_pos(case)
    output.append(str(result))

    return sum_of_positive_integers(input, output)


def main():
    # estimate the number of lines need to be read
    lines = 2 * int(stdin.readline())

    if lines <= 0:
        print("Number of cases must be positive and greater than 0")
        return

    # load input from stdin
    inputs = read_input_from_std([], lines)

    # process the input
    outputs = sum_of_positive_integers(inputs, [])

    # print the output
    print("\n".join(outputs))


if __name__ == "__main__":
    main()