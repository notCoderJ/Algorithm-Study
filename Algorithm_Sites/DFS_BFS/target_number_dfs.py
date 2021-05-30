def dfs(res, lv, numbers, target):
    if lv == len(numbers):
        if res == target:
            return 1
        else:
            return 0
        
    cnt = 0
    cnt += dfs(res + numbers[lv], lv + 1, numbers, target)
    cnt += dfs(res - numbers[lv], lv + 1, numbers, target)
    
    return cnt
            
def solution(numbers, target):
    answer = dfs(0, 0, numbers, target)
    
    return answer