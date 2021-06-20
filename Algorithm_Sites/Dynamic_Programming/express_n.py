def solution(N, number):
    if N == number: # N과 number가 동일하면 1을 즉시 반환한다
        return 1
    
    answer = -1
    dp = [set()] # 1 ~ 8 사용 횟수를 맞추기 위한 0번 공집합 추가
    for i in range(1, 9):
        valid = [int(str(N) * i)] # 사용 횟수만큼 이어붙인 수
        for j in range(1, i):
            for a in dp[j]:
                for b in dp[i - j]:
                    valid += [val for val in (a + b, a - b, a * b, a // b) if val > 0]
        if number in valid:
            answer = i
            break;
        else:
            dp.append(set(valid))

    return answer


import unittest as ut

class TestExpressN(ut.TestCase):
    def test_solution(self):
        self.assertEqual(solution(5, 12), 4)
        self.assertEqual(solution(5, 31168), -1)

ut.main()