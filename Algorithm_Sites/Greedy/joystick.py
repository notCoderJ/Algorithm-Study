def solution(name):
    answer = 0
    cursor = 0
    back = False
    for i in range(len(name)):
        if name[i] != 'A':
            if len(name) - 1 - cursor > cursor + len(name) - i:
                back = True
                answer += cursor + len(name) - i
            answer += i - cursor if not back else 0
            answer += min(ord(name[i]) - ord('A'), ord('Z') - ord(name[i]) + 1)
            cursor = i
    
    return answer