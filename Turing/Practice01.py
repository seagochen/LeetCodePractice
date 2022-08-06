def count_records(opts: list):
    result = 0

    temp_list = []

    for opt in opts:
        if opt != "C" and opt != "D" and opt != "+":
            num = int(opt)
            temp_list.append(num)
        if opt == "C":
            temp_list.pop()
        if opt == "D":
            t = temp_list.pop()
            dt = t * 2
            temp_list.extend([t, dt])
        if opt == "+":
            t2 = temp_list.pop()
            t1 = temp_list.pop()
            t3 = t1 + t2
            temp_list.extend([t1, t2, t3])

    for n in temp_list:
        result += n

    return result


if __name__ == "__main__":
    test_case_1 = ["5", "2", "C", "D", "+"]
    test_result_1 = count_records(test_case_1)
    print(test_result_1)
