def odd_series_conditional(a):
    count = a if a % 2 != 0 else a - 1
    result = [2 * i + 1 for i in range(count)]
    print(", ".join(map(str, result)))

odd_series_conditional(4)
