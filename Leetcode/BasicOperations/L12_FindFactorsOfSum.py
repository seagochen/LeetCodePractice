def solution(numbers, target):

    # Create a dict of sticks
    numb_dict = {numb: True for numb in numbers}

    # Loop through sticks
    for numb in numbers:
        # If the target - stick is in the dict
        if target - numb in numb_dict:
    
            # Return the pair
            return [numb, target - numb]

    # If no pair is found, return None
    return []

def main():
    print(solution([1, 2, 3, 9], 8))
    print(solution([1, 2, 4, 4], 8))

if __name__ == "__main__":
    main()