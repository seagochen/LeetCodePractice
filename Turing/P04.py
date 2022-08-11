def solution(window_size, numbers):
    result = []
    window = []
    for number in numbers:
        window.append(number)
        if len(window) == window_size:
            result.append(max(window))
            window.pop(0)
    return result

def main():
    print(solution(3, [1, 3, -1, -3, 5, 3, 6, 7]))
    print(solution(2, [1, 3, -1, -3, 5, 3, 6, 7]))
    print(solution(1, [1, 3, -1, -3, 5, 3, 6, 7]))

if __name__ == "__main__":
    main()