# 문제를 조금 변형하여
# n*m 크기의 얼음틀이 주어졌을 때 생성되는 아이스크림의 크기와 총 개수를 알아보자.
# 구멍이 뚫린 부분은 0, 막힌 부분은 1이고 구멍이 뚫린 부분끼리 상하좌우 붙어있으면 연결된 것으로 한다.

# 문제 파악 포인트:
#   1. 얼음판의 구멍 뚫린 위치에서 상하좌우로 연결된 부분이 있는지 탐색을 요구한다
#   2. 단순한 영역 탐색이다
#   따라서, DFS나 BFS 알고리즘을 적용해 해결할 수 있다

n, m = map(int, input().split())
ice_plate = [list(map(int, input())) for _ in range(n)]

# *** dfs 알고리즘을 이용한 풀이 ***
def dfs(x, y):
    # 얼음판 범위를 초과하거나 막혀있으면 종료
    if x < 0 or x > n-1 or y < 0 or y > m-1 or ice_plate[x][y] == 1:
        return 0 # False

    ice_plate[x][y] = 1 # 현재 뚫린 부분에 아이스크림을 넣는다
    size = 1 # 아이스크림 크기를 계산한다
    # 현재 위치에서 상하좌우 연결된 부분에 대해 dfs를 수행한다
    size += dfs(x-1, y) # 상
    size += dfs(x+1, y) # 하
    size += dfs(x, y-1) # 좌
    size += dfs(x, y+1) # 우

    return size # True

# *** bfs 알고리즘을 이용한 풀이 ***
from collections import deque

def bfs(x, y):
    if ice_plate[x][y] == 1: # 막혀있으면 종료
        return 0 # False

    queue = deque([(x, y)])
    ice_plate[x][y] = 1 # 현재 뚫린 부분에 아이스크림을 넣는다
    size = 0

    while queue:
        cx, cy = queue.popleft()
        size += 1 # 아이스크림이 들어있는 부분을 계산한다
        # 현재 위치의 상하좌우에 구멍이 뚫린 부분이 있으면 아이스크림을 넣는다
        u, d, l, r = cx - 1, cx + 1, cy - 1, cy + 1
        if u >= 0 and ice_plate[u][cy] == 0:
            queue.append((u, cy))
            ice_plate[u][cy] = 1
        if d < n and ice_plate[d][cy] == 0:
            queue.append((d, cy))
            ice_plate[d][cy] = 1
        if l >= 0 and ice_plate[cx][l] == 0:
            queue.append((cx, l))
            ice_plate[cx][l] = 1
        if r < m and ice_plate[cx][r] == 0:
            queue.append((cx, r))
            ice_plate[cx][r] = 1

    return size # True

count = 0
ice_cream = []
for x in range(n):
    for y in range(m):
        ice_cream_size = dfs(x, y)
        # ice_cream_size = bfs(x, y)
        if ice_cream_size != 0:
            ice_cream.append(ice_cream_size)

print("아이스크림 크기 :", ice_cream, "아이스크림 총 개수 :", len(ice_cream))

''' TEST CASE
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111
''' # count 8