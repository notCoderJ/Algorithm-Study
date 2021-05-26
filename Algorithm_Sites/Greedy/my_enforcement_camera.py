def solution(routes):
    answer = 0
    routes.sort() # 이동 경로의 진입점을 기준으로 오름차순으로 정렬한다
    last_exit = -30001

    for s, e in routes:
        if s <= last_exit:
            if e < last_exit:
                last_exit = e
        else:
            answer += 1
            last_exit = e
    
    return answer