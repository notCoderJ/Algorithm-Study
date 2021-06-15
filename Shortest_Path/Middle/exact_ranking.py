# N명의 시험 성적을 분실하고 성적을 비교한 결과만 일부 가지고 있을 때
# 성적 순위를 정확히 알 수 있는 학생은 모두 몇명인가?
# ex) 학생 6명의 성적을 비교한 결과가 다음과 같다면
#   1 < 5
#   3 < 4
#   4 < 2
#   4 < 6
#   5 < 2
#   5 < 4
# 4번 학생보다 성적이 낮은 학생은 3명, 높은 학생은 2명이므로
# 4번 학생의 순위를 정확히 알 수 있다.

# 풀이 전략
'''
    각 학생들을 그래프의 노드로 생각하면 1 < 5는 1 -> 5와 같은 방향 그래프로 표현할 수 있고,
    정확한 순위를 안다는 것은 해당 노드에서 다른 모든 노드로 가는 경로가 있다는 것이다.
    따라서, 플로이드 워셜 알고리즘을 이용해 각 노드 간의 경로가 존재하는지 확인하면 된다!
'''

INF = int(1e9)


# 처음으로 풀이한 코드
def my_solve_floyd(n, ranking):
    rank = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        rank[i][i] = 0 # 자기 자신은 0으로 초기화

    for a, b in ranking: # 성적: a < b를 의미
        rank[a][b] = 0 # a가 b보다 낮을 때 0 높을 때 1
        rank[b][a] = 1

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                # 중간 학생과 비교 값이 같다는 것은 두 학생의 순위를 비교할 수 있다는 것이다
                if rank[j][i] == rank[i][k] and rank[j][i] != INF:
                    rank[j][k] = rank[j][i]

    students = 0

    for student in rank[1:]:
        if INF not in student[1:]: # 모든 학생들과 순위 비교가 가능한 학생을 카운트한다
            students += 1

    return students


# 풀이를 참고해 생각해본 좀 더 간결한 방법의 코드
def solve_floyd(n, ranking):
    rank = [[False] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        rank[i][i] = True # 자기 자신으로의 경로는 항상 True이다

    for a, b in ranking: # 성적: a < b를 의미
        rank[a][b] = True # a < b일 때 True(즉, a에서 b로 가는 경로가 존재한다)

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                # 중간 학생을 거쳐서 가는 경로가 있는지 확인한다
                rank[j][k] = rank[j][k] or rank[j][i] and rank[i][k]

    students = 0

    for a in range(1, n + 1):
        path = 0
        for b in range(1, n + 1):
            if any((rank[a][b], rank[b][a])): # 한 쪽 방향의 경로가 존재하는지 확인한다
                path += 1
        if path == n:
            students += 1
    
    return students


n, m = map(int, input().split())
ranking = [tuple(map(int, input().split())) for _ in range(m)]

print(my_solve_floyd(n, ranking))
print(solve_floyd(n, ranking))


''' TEST1
6 6
1 5
3 4
4 2
4 6
5 2
5 4
''' # 1
''' TEST2
5 5
1 3
3 2
5 2
4 5
3 4
''' # 5


import unittest as ut

# 테스트 코드
class TestExactRanking(ut.TestCase):
    def test_my_solve(self):
        self.assertEqual(my_solve_floyd(n, ranking), 1) # TEST1
        # self.assertEqual(my_solve_floyd(n, ranking), 5) # TEST2

    def test_solve(self):
        self.assertEqual(solve_floyd(n, ranking), 1) # TEST1
        # self.assertEqual(solve_floyd(n, ranking), 5) # TEST2

ut.main()