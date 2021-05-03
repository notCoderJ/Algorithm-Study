# 1 x 1 크기의 칸으로 나누어져 있는 n x m 금광에 각 칸마다 특정 크기의 금이 들어있을 때
# 다음 조건을 만족하며 금을 캘 때 최대 얻을 수 있는 금의 크기는?
# 조건 :
#   1. 첫 번째 열부터 금을 캐기 시작하며, 맨 처음에는 어느 행에서든 출발할 수 있다.
#   2. 이후 m번에 걸쳐 매번 오른쪽 위, 오른쪽, 오른쪽 아래 중 선택 후 이동해야 한다.

# 풀이 전략
'''
    2차원 금광 내 임의의 칸을 (i, j)라 할 때 해당 칸에 접근하는 경우의 수는 다음과 같다.
    1. 왼쪽 위에서 접근 (i-1, j-1)
    2. 왼쪽에서 접근 (i, j-1)
    3. 왼쪽 아래에서 접근 (i+1, j-1)
    
    현재 칸(i, j)에 있는 금의 양을 g라 할 때
    해당 문제의 점화식은 a(i, j) = g + max(a(i-1, j-1), a(i, j-1), a(i+1, j-1))이 된다.
'''

for _ in range(int(input())):
    n, m = map(int, input().split())
    gold = list(map(int, input().split()))

    # 금광 내 각 위치에서 채굴한 금의 최대값을 기록할 dp 테이블 초기화
    dp = []
    idx = 0
    for _ in range(n):
        dp.append(gold[idx:idx + m])
        idx += m

    # 다이나믹 프로그래밍 수행
    for c in range(1, m):
        for r in range(n):
            left = dp[r][c-1]
            if r == 0: # 첫 번째 행 == 왼쪽 위 접근 X
                left_top = 0
            else:
                left_top = dp[r-1][c-1]
            if r == n - 1: # 마지막 행 == 왼쪽 아래 접근 X
                left_down = 0
            else:
                left_down = dp[r+1][c-1]
            dp[r][c] = dp[r][c] + max(left, left_top, left_down)

    max_gold = 0
    for i in range(n):
        max_gold = max(max_gold, dp[i][m - 1])

    print(max_gold)


''' TEST
2 
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
''' # 19 16