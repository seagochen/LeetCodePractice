# generate final test case

def increase_digits(numbers = 100):
    for i in range(1, numbers+1):
        print(i)
        for j in range(1, i+1):
            print(1, end=" ")
        print(end="\n")

increase_digits(120)