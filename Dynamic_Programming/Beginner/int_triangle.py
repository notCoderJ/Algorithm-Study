# 한 변의 크기가 N인 정수 삼각형에서 맨 위층부터 시작해 아래에 있는 수 중 하나를 선택하며
# 아래층으로 내려올 때 선택한 수들의 함이 최대가 되는 경로는?
# (단, 선택 가능한 수는 현재 층의 선택한 수에서 좌측, 우측 대각선에 있는 수만 선택가능)
# 아래는 크기가 5인 정수 삼각형의 예시 7 > 3 > 8 > 7 > 5 순으로 선택해야 최대가 됨.
#     7
#    3 8
#   8 1 0
#  2 7 4 4
# 4 5 2 6 5

# 풀이 전략
'''
    해당 층에서 합이 최대인 경로는 해당 층의 각 지점 값에
    좌측, 우측 대각선에 있는 이전 층의 값 중 큰 값을 더하여
    해당 층의 값들을 모두 갱신한 후 그 중 최대값을 고르면 된다.

    따라서, 각 층의 지점에 대해 다음과 같은 점화식을 세울 수 있다.
    (i는 현재 층을, j는 해당 층 내 지점을 의미한다.)
    a(i, j) = a(i, j) + max(a(i-1, j-1), a(i-1, j))
'''


n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]


# 풀이 1: 다이나믹 프로그래밍
'''
    높이가 N인 정수 삼각형이라고 할 때 시간 복잡도를 계산해보면
    한 층씩 내려갈 때마다 해당 층의 원소 개수만큼씩 연산이 추가된다.
    따라서, N층에서의 연산 횟수는 1 + 2 + 3 + ... + N이므로
    시간 복잡도는 약 O(N²)이라고 할 수 있다.
'''
def solve_dynamic(n, triangle):
    for floor in range(1, n):
        for i in range(floor + 1):
            left = 0
            right = 0
            if i != 0: # 좌측 상단에서 내려오는 경우
                left = triangle[floor-1][i-1]
            if i != floor: # 우측 상단(동일 인덱스)에서 내려오는 경우
                right = triangle[floor-1][i]
            triangle[floor][i] += max(left, right)
    return max(triangle[n - 1])


# 풀이 2: Top-down방식의 다이나믹 프로그래밍(== DFS)
'''
    시간 복잡도는 함수 호출로 인한 오버 헤드를 제외하면 위와 비슷하다고 볼 수 있다.
    하지만 2차원 메모이제이션 테이블을 생성해야 하므로 불필요한 메모리 낭비가 발생한다.
'''
memo = [[-1] * n for _ in range(n)]

def solve_dfs(start, floor, n, triangle):
    if floor + 1 == n:
        return triangle[floor][start]
    else:
        # 좌측 하단으로 내려가는 경우
        left = solve_dfs(start, floor + 1, n, triangle) if memo[floor + 1][start] == -1 else memo[floor + 1][start]
        # 우측 하단으로 내려가는 경우
        right = solve_dfs(start + 1, floor + 1, n, triangle) if memo[floor + 1][start + 1] == -1 else memo[floor + 1][start + 1]
        memo[floor][start] = triangle[floor][start] + max(left, right)

        return memo[floor][start]


''' TEST
5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
''' # 30

import unittest

class TestIntTriangle(unittest.TestCase):
    def test_solve_dynamic(self):
        self.assertEqual(solve_dynamic(n, triangle), 30)

    def test_solve_dfs(self):
        self.assertEqual(solve_dfs(0, 0, n, triangle), 30)

unittest.main()