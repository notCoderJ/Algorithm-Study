def solution(N, stages):
    answer = []

    fail = {}
    user_cnt = len(stages)

    for stage in range(1, N + 1):
        if user_cnt:
            in_challenge = stages.count(stage)
            fail[stage] = in_challenge / user_cnt
            user_cnt -= in_challenge
        else:
            fail[stage] = 0

    answer = sorted(fail, key=lambda x: fail[x], reverse=True)
    return answer
