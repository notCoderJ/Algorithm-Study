# 8*8 체스판 내 특정 위치에 있는 나이트가 다음 조건 하에 이동할 수 있는 모든 경우의 수?
#   1. 나이트는 'L'자로만 이동가능 (수평 2 + 수직 1 or 수직 2 + 수평 1)
#   2. 체스판 밖으로 나갈 수 없다
#   3. 행은 1~8, 열은 a~h

# 문제 유형:
#   제한된 조건 내에 이동 가능한 모든 경우의 수를 구하므로 '완전 탐색' 유형에 속한다

# 문자인 열의 좌표 계산을 위해 ord, chr 함수를 기억하자!
#   ord : 문자를 아스키 코드 값으로 계산해준다 / chr : 아스키 코드 값을 문자로 표시해준다

knight_pos = input()

# 이동 경로에 대한 좌표를 정의
move_case = [(-1, 2), (-1, -2), (1, 2), (1, -2), (-2, -1), (-2, 1), (2, -1), (2, 1)]

knight_x, knight_y = int(knight_pos[1]), ord(knight_pos[0])

count = 0
for dx, dy in move_case:
    next_x, next_y = knight_x + dx, knight_y + dy # 나이트가 이동할 다음 좌표를 구한다
    if next_x >= 1 and next_x <= 8 and next_y >= ord('a') and next_y <= ord('h'):
        count += 1 # 체스판 내에서 이동할 경우만 카운트 해준다

print (count)