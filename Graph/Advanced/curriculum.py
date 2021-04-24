# 1 ~ N번의 강의가 있을 때 N개의 강의를 수강하는 데 걸리는 최소 시간?
# 조건 :
#   1. 선수 강의가 있는 강의는 선수 강의를 먼저 수강해야 한다.
#   2. 동시에 여러 개의 강의를 수강할 수 있다.

# 문제 풀이 전략
'''
    1. 특정 강의를 수강하는데 선수 강의가 존재할 수 있고
        정해진 순서대로 강의를 수강해야 하므로 위상 정렬 알고리즘을 사용할 수 있다.
    2. 동시에 여러 개의 강의를 수강할 수 있으므로 선수 강의가 다수인 경우에도
        모두 동시에 수강하면 된다. 하지만 강의 시간은 서로 다를 수 있으므로
        강의 시간 중 가장 긴 시간을 선수 강의가 종료되는 시간으로 계산하면 된다.
'''

from collections import deque
# import copy


# 강의 수 입력
n = int(input())

def topology_sort(graph, indegree, time):
    q = deque()
    result = [0] * (n + 1) # 강의마다 걸리는 최소 수강 시간을 저장할 리스트 초기화
    # copy 라이브러리의 deepcopy 함수를 이용해 time 리스트 전체를 복사해 초기화할 수도 있다.
    # result = copy.deepcopy(time)

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
            result[i] = time[i]

    while q:
        current = q.popleft()
        for i in graph[current]:
            # 기존 수강 시간과 현재 수강 시간 중 더 오래걸리는 값으로 갱신
            result[i] = max(result[i], result[current] + time[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in result[1:]:
        print(i)


# 진입차수 초기화
indegree = [0] * (n + 1)

# 선수 강의 정보를 저장할 그래프
graph = [[] for _ in range(n + 1)]

# 각 강의 시간 초기화
time = [0] * (n + 1)

# 강의 시간 및 선수 강의 번호 입력
for i in range(1, n + 1):
    lecture_info = list(map(int, input().split()))
    time[i] = lecture_info[0]
    indegree[i] = len(lecture_info) - 2
    for j in lecture_info[1:-1]:
        graph[j].append(i)

topology_sort(graph, indegree, time)


''' TEST
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1
''' # 10 20 14 18 17