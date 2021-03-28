# n*m 직사각형 미로에서 괴물을 피해 탈출할 때 움직여야 하는 최소 칸수?
# 괴물이 있는 곳은 0, 없는 곳은 1이며 미로는 반드시 탈출 가능하다.
# 시작과 마지막 칸을 모두 카운팅한다.

# 문제 파악 포인트:
#   1. 미로 내 현재 위치에서 상하좌우로 이동 가능한 위치가 있는지 탐색을 요구한다
#   2. 최단 경로를 알기 위해 이동 거리의 비교가 필요하다
#   따라서, BFS 알고리즘을 적용해 해결할 수 있다

n, m = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]

# *** bfs 알고리즘을 이용한 풀이 ***
from collections import deque

def bfs(x, y):
    start_x, start_y = x-1, y-1 # 미로는 (0, 0)부터 시작
    queue = deque([(start_x, start_y)])

    # 시작 위치 값이 1이므로 이후 진행에서 재방문으로 인해 값이 변경된다
    # 하지만 출구가 항상 2차원 배열의 끝이므로 결과에 영향을 주지 않는다 
    while queue:
        cx, cy = queue.popleft()
        if cx == n-1 and cy == m-1: # 미로의 출구에 도착했으면 그 거리를 리턴한다
            return maze[n-1][m-1]
        # 현재 위치에서 상하좌우에 이동 가능한 위치가 있으면 그 위치 값에 현재까지의 거리를 합한다
        udlf = [(cx-1, cy), (cx+1, cy), (cx, cy-1), (cx, cy+1)]
        for nx, ny in udlf:
            if nx < 0 or nx >= n or ny < 0 or ny >= m: # 미로 범위를 벗어나면 무시
                continue
            if maze[nx][ny] == 1:
                queue.append((nx, ny))
                maze[nx][ny] += maze[cx][cy]
    return 0

print("최소 이동 칸수 :", bfs(1, 1))
''' TEST CASE
5 6
101010
111111
000001
111111
111111
''' # count 10