def solution(routes):
    answer = 0
    routes.sort(reverse=True) # 이동 경로의 진입점을 기준으로 내림차순으로 정렬한다
    last_camera = 30001

    for s, e in routes:
        if last_camera > e:
            answer += 1
            last_camera = s

    return answer