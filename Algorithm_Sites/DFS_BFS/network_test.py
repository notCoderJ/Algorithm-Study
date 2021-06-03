import random

def solution(n, computers): # 수정 버전
    network_map = [ computer for computer in range(n)]
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                for k in range(n):
                    if network_map[k] == network_map[j]:
                        network_map[k] = network_map[i]
                        print(network_map)
    return network_map, len(set(network_map))

def solution_answer(n, computers): # 수정전 풀이 코드
    network_map = [ computer for computer in range(n)]
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                for k in range(n):
                    if network_map[k] == network_map[i]:
                        network_map[k] = network_map[j]
    return network_map, len(set(network_map))

# 랜덤으로 생성한 컴퓨터 연결 리스트 출력 함수
def print_2d_list(n, arry):
    for i in range(n):
        for j in range(n):
            print(arry[i][j], end=' ')
        print()

# 알고리즘 비교 무한 루프
while True:
    n = random.randrange(1, 6)
    computers = [[-1] * n for i in range(n)]

    for i in range(n):
        computers[i][i] = 1

    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == -1:
                val = random.randrange(0, 2)
                computers[i][j], computers[j][i] = val, val

    network1, cnt1 = solution(n, computers)
    network2, cnt2 = solution_answer(n, computers)
    print(cnt1, cnt2)
    if cnt1 != cnt2: # 두 알고리즘의 결과가 다를 경우 관련 정보들을 출력하고 종료
        print_2d_list(n, computers)
        print()
        print(network1)
        print()
        print(network2)
        break
        