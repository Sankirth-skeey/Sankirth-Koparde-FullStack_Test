def odd_series(a):
    result = [2 * i + 1 for i in range(a)]
    print(", ".join(map(str, result)))

odd_series(4)
