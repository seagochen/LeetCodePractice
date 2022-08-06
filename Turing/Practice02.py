def is_valid(s: str):
    input_c = list(s)
    flag = 0        # 0: start
                    # 1: {
                    # 2: [
                    # 3: (

    for c in input_c:
        if flag == 0:
            if c == "{":
                flag = 1
                continue
            if c == "[":
                flag = 2
                continue
            if c == "(":
                flag = 3
                continue
            return False
        elif flag == 1:
            if c != "}":
                return False
            else:
                flag = 0
        elif flag == 2:
            if c != "]":
                return False
            else:
                flag = 0
        elif flag == 3:
            if c != ")":
                return False
            else:
                flag = 0

    return True

if __name__ == "__main__":
    line1 = "()[]{}"
    line2 = "()[]}"

    res1 = is_valid(line1)
    res2 = is_valid(line2)

    print(res1, res2)