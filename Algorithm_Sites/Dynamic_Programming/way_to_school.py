def solution(m, n, puddles):
    answer = 0
    # 초기 값을 -1로 설정하여 물 웅덩이의 값인 0과 차이를 둠으로써
    # 물 웅덩이가 아닌 지점에 대해서만 도착 경우의 수를 구하면서
    # 물 웅덩이에서 오는 경우는 0 값이 더해지도록 하였다.
    path_cnt = [[-1] * (n + 1) for _ in range(m + 1)]
    path_cnt[1][1] = 1
    for x, y in puddles:
        path_cnt[x][y] = 0

    for x in range(1, m + 1):
        for y in range(1, n + 1):
            if path_cnt[x][y] == -1:
                up, left = 0, 0
                if x - 1 > 0:
                    up = path_cnt[x - 1][y]
                if y - 1 > 0:
                    left = path_cnt[x][y - 1]
                path_cnt[x][y] = up + left

    divisor = 1000000007
    answer = path_cnt[m][n] % divisor

    return answer
