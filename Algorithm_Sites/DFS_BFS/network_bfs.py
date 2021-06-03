from collections import deque

def bfs(start, connected, n, computers):
    q = deque([start])
    connected[start] = True

    while q:
        current = q.popleft()
        for i in range(n):
            if not connected[i] and computers[current][i] == 1:
                connected[i] = True
                q.append(i)

def solution(n, computers):
    answer = 0
    connected = [False] * n
    for i in range(n):
        if not connected[i]:
            bfs(i, connected, n, computers)
            answer += 1
    
    return answer