def solution(n, computers):
    network_map = [ computer for computer in range(n)]
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                for k in range(n):
                    if network_map[k] == network_map[i]:
                        network_map[k] = network_map[j]
    return len(set(network_map))