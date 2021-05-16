# My Code - 최대힙 방식의 우선순위 큐를 활용한 풀이
# 최악의 경우는 큐에 삽입, 삭제 연산이 가장 많이 발생하는 k = 1일 때라고 생각한다.
# 예상 시간 복잡도 :
#   1. 우선순위 큐에 N개의 원소 삽입 연산 : NlogN
#   2. 우선순위 큐에서 N개의 원소 삭제 연산 : NlogN
# 따라서, NlogN + NlogN = 2NlogN이므로 약 O(NlogN)의 시간 복잡도가 소요된다고 할 수 있다.
# (N개의 원소에 대한 우선순위 큐의 삽입, 삭제 연산이 각각 O(logN)이므로)
import heapq

def solution(number, k):
    answer = ''
    q = []
    cmp_range = k + 1
    for i in range(cmp_range):
        heapq.heappush(q, (-int(number[i]), i))
    text_cnt = len(number) - k
    pre_idx = -1
    while True:
        cur_val, cur_idx = heapq.heappop(q)
        if cur_idx > pre_idx:
            answer += str(-cur_val)
            pre_idx = cur_idx
            text_cnt -= 1
            if text_cnt == 0:
                break
            heapq.heappush(q, (-int(number[cmp_range]), cmp_range))
            cmp_range += 1
            
    return answer


# Other Code - 스택을 활용한 풀이*** (대~박)
# 예상 시간 복잡도 :
#   1. 스택에 N개의 원소 삽입 연산 : N
#   2. 스택에서 K개의 원소 삭제 연산 : K
# 따라서, 약 O(N + K)의 시간 복잡도가 소요된다고 할 수 있다.

def solution(number, k):
    answer = ''
    stack = []
    for i in range(len(number)):
        # 스택에 데이터가 들어있고 제거할 횟수(k)가 남아있으면
        # 현재 위치 값보다 스택의 마지막 데이터 값이 작은 경우 스택의 Top에서 데이터를 제거한다
        while stack and k > 0 and stack[-1] < number[i]:
            stack.pop()
            k -= 1
        stack.append(number[i])
    answer = ''.join(stack[:len(stack) - k]) # 범위 제한은 k != 0를 고려함(뒷부분 데이터가 내림차순인 경우)
    
    return answer