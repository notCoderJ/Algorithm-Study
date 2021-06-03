def dfs(start, connected, n, computers):
    if connected[start] == True:
        return False

    connected[start] = True
    
    for i in range(n):
        if computers[start][i] == 1:
            dfs(i, connected, n, computers)
            
    return True

def solution(n, computers):
    answer = 0
    connected = [False] * n
    for i in range(n):
        if dfs(i, connected, n, computers) == True:
            answer += 1
    
    return answer