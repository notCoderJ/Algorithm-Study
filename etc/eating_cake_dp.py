def impossible_max_cnt(n1, n2, n3):
    pass_numbers = []
    minimum = min(n1, n2, n3)
    maximum = max(n1, n2, n3)
    dp = [False for _ in range(maximum + 1)]
    dp[0] = True
    for i in [n1, n2, n3]:
        dp[i] = True

    for num in range(minimum, maximum + 1):
        if dp[num - n1] or num >= n2 and dp[num - n2] or num >= n3 and dp[num - n3]:
            dp[num] = True
            pass_numbers.append(num)
        else:
            pass_numbers = []
        if len(pass_numbers) >= minimum:
            return pass_numbers[0] - 1

    # 상자의 최대 크기보다 큰 범위에 대해 확인한다
    pass_numbers = []
    num = maximum + 1
    while len(pass_numbers) < minimum:
        dp.append(False)
        if dp[num - n1] or dp[num - n2] or dp[num - n3]:
            dp[num] = True
            pass_numbers.append(num)
        else:
            pass_numbers = []
        num += 1

    return pass_numbers[0] - 1

print(impossible_max_cnt(7, 11, 17))
