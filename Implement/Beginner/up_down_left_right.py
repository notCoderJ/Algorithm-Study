# 1*1크기로 나누어진 N*N 정사각형 공간에서 A가 다음과 같은 조건 하에 이동할 때 최종적으로 도착할 지점의 좌표는?
#   1. 시작 좌표는 항상 (1, 1)이며, 상하좌우(UDLR) 한 방향으로만 이동 가능
#   2. N*N을 벗어나는 움직임은 무시됨

# 문제 유형:
#   개체를 주어진 명령에 따라 차례로 이동시키므로 '시뮬레이션' 유형에 속한다

n = int(input())
move_plan = input().split()

# 이동 경로에 대한 좌표를 정의
move_case = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
A_pos_x, A_pos_y = 1, 1

for i in move_plan:
    dx, dy = move_case[i]
    next_x, next_y = A_pos_x + dx, A_pos_y + dy # A가 이동할 다음 좌표를 구한다

    if next_x < 1 or next_x > n or next_y < 1 or next_y > n:
        continue # 공간을 벗어날 경우 무시
    
    A_pos_x, A_pos_y = next_x, next_y # A의 현재 좌표를 갱신한다

print(A_pos_x, A_pos_y)