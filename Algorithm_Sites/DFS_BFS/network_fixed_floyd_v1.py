def solution(n, computers):
    network_map = [ computer for computer in range(n)]
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                for k in range(n):
                    if network_map[k] == network_map[j]: # 수정 부분: 인덱스 i -> j
                        network_map[k] = network_map[i] # 인덱스 j -> i
                        print(network_map)
    return network_map, len(set(network_map))