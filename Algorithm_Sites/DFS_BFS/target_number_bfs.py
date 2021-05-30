from collections import deque
    
def solution(numbers, target):
    q = deque([(0, 0)])
    answer = 0

    while q:
        res, lv = q.popleft()
        if lv == len(numbers):
            if res == target:
                answer += 1
        else:
            q.append((res + numbers[lv], lv + 1))
            q.append((res - numbers[lv], lv + 1))
    
    return answer