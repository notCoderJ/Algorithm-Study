# 1*1 크기로 이루어진 N*M 직사각형 공간에 있는 캐릭터를 다음 조건을 만족시키며 매뉴얼에 따라 이동시킬 때 방문한 칸 수?
#   1. 각각 칸은 육지와 바다이며 바다로 된 공간엔 갈 수 없다
#   2. 캐릭터는 동서남북 중 한 곳을 향한다
#   3. 각 칸은 (A, B)로 나타내며 A는 북쪽에서 떨어진 칸 수, B는 서쪽에서 떨어진 칸 수를 의미한다
#   4. 맵의 외관은 항상 바다로 되어있다.
# 매뉴얼
#   1. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 차례로 갈 곳을 정한다
#   2. 캐릭터 왼쪽 방향에 가보지 않은 칸이 존재하면 왼쪽으로 회전 후 1칸 이동, 가보지 않은 칸이 없다면 회전만 하고 1번을 재수행
#   3. 네 방향 모두 이미 가본 칸이거나 바다로 되어 있으면 바라보는 방향을 유지하고 한 칸 뒤로 간 후 1번 수행
#       (단, 뒤쪽 방향이 바다인 경우 움직임을 멈춤)
# 육지(0), 바다(1), 동서남북(1,3,2,0)

n, m = map(int, input().split())
user_x, user_y, direction = map(int, input().split())
game_map = [list(map(int, input().split())) for _ in range(n)]

# 동서남북 각 방향의 이동 경로에 대한 좌표 정의
move_case = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 북, 동, 남, 서

game_map[user_x][user_y] = 2 # 처음 위치 방문 표시
count = 1 # 처음 위치 카운팅
block = 0 # 이동 가능 방향 검사
while True:
    direction = direction - 1 if direction - 1 >= 0 else 3 # 현재 위치의 서쪽 방향으로 방향 변경
    next_x, next_y = user_x + move_case[direction][0], user_y + move_case[direction][1]
    if game_map[next_x][next_y] == 0: # 현재 방향에 방문하지 않았는지 검사
        user_x, user_y = next_x, next_y
        game_map[user_x][user_y] = 2 # 현재 이동한 위치 방문 표시
        count += 1
        block = 0
        continue
    else: # 현재 방향에서 이동이 불가능할 경우(바다or 방문한 곳)
        block += 1

    if block == 4: # 네 방향이 모두 막혀있거나 방문헀던 곳일 경우
        next_x, next_y = user_x - move_case[direction][0], user_y - move_case[direction][1]
        if game_map[next_x][next_y] == 1: # 뒤쪽이 바다인 경우
            break
        user_x, user_y = next_x, next_y
        block = 0

print(count)