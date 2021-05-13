def impossible_max_cnt(n1, n2, n3):
    pass_numbers = []
    minimum = min(n1, n2, n3)
    num = minimum
    make = False
    
    while len(pass_numbers) < minimum:
        # 각 상자의 크기에 대해 사용 가능한 최대 개수를 구한다
        cnt_n1, cnt_n2, cnt_n3 = num // n1, num // n2, num // n3
        for i in range(cnt_n1 + 1):
            for j in range(cnt_n2 + 1):
                for k in range(cnt_n3 + 1):
                    if n1 * i + n2 * j + n3 * k == num:
                        pass_numbers.append(num)
                        make = True
                        break
                else: # for문의 else문은 for문의 반복 횟수를 모두 수행한 경우만 실행된다.
                    continue
                break
            else:
                continue
            break

        if not make:
            pass_numbers = []
        else:
            make = False
            
        num += 1

    return pass_numbers[0] - 1

print(impossible_max_cnt(7, 11, 17))
