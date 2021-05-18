import heapq

def solution(number, k):
    answer = ''
    q = []
    cmp_range = k + 1
    for i in range(cmp_range):
        heapq.heappush(q, (-int(number[i]), i)) # 음수 값으로 넣어 최대힙으로 동작
    text_cnt = len(number) - k
    pre_idx = -1
    while True:
        cur_val, cur_idx = heapq.heappop(q)
        if cur_idx > pre_idx: # 현재 인덱스가 이전 인덱스보다 작은 경우 이미 제거한 숫자임
            answer += str(-cur_val)
            pre_idx = cur_idx
            text_cnt -= 1
            if text_cnt == 0:
                break
            heapq.heappush(q, (-int(number[cmp_range]), cmp_range))
            cmp_range += 1
            
    return answer