def solution(n, computers):
    network_map = [ computer for computer in range(n)]
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                connected = network_map[j] # 연결된 네트워크를 저장해놓는다
                for k in range(n):
                    if network_map[k] == connected:
                        network_map[k] = network_map[i]
    return len(set(network_map))