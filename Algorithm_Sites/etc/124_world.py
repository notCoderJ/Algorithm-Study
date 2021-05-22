def solution(n):
    answer = ''

    while n:
        n, r = divmod(n, 3)
        answer = '412'[r] + answer
        if r == 0:
            n -= 1

    return answer