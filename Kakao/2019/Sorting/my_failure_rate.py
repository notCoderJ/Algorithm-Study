def solution(N, stages):
    answer = []

    in_challenge = [0] * (N + 2)
    for i in range(1, N + 2):
        in_challenge[i] = stages.count(i)

    for stage in range(1, N + 1):
        if not in_challenge[stage]:
            answer.append((0, stage))
        else:
            answer.append((in_challenge[stage] / sum(in_challenge[stage:]),
                           stage))

    answer.sort(key=lambda x: (-x[0], x[1]))
    answer = list(map(lambda x: x[1], answer))

    return answer
