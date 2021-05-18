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