def tribonacci_sequence(start_sequence, length):
    fibonacci = []

    if length <= 0: return fibonacci

    if length <= 3:
        for x in range(length):
            fibonacci.append(start_sequence[x])
    else:
        t1, t2, t3 = start_sequence[0], start_sequence[1], start_sequence[2]
        fibonacci = [t1, t2, t3]
        for x in range(0, length - 3):
            t4 = t1 + t2 + t3

            t1 = t2
            t2 = t3
            t3 = t4
            fibonacci.append(t4)

    return fibonacci

print(tribonacci_sequence([123, 456, 789], 4))