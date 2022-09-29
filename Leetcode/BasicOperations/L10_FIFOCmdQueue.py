def solution(capacity, commands):
    queue = []
    result = []
    for command in commands:
        if command.startswith("OFFER"):
            if len(queue) < capacity:
                queue.append(command.split(" ")[1])
                result.append("true")
            else:
                result.append("false")
        elif command.startswith("TAKE"):
            if len(queue) > 0:
                result.append(queue.pop(0))
        elif command.startswith("SIZE"):
            result.append(str(len(queue)))
    return result

def main():
    print(solution(2, ["OFFER 1", "OFFER 2", "OFFER 3", "TAKE 2", "TAKE 2", "SIZE"]))
    print(solution(1, ["OFFER 1", "OFFER 2", "TAKE 2", "TAKE 2", "SIZE"]))
    print(solution(1, ["OFFER 1", "OFFER 2", "TAKE 2", "TAKE 2", "OFFER 3", "SIZE"]))

if __name__ == "__main__":
    main()
