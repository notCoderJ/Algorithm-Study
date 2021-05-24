def solution(people, limit):
    answer = 0
    stack = []
    people.sort(reverse=True)
    
    for i in people:
        if stack and stack[-1] + i <= limit:
            answer += 1
            stack.pop()
        else:
            stack.append(i)
            
    if stack:
        answer += len(stack)

    return answer