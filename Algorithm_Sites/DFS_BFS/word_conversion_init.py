def dfs(begin, target, words):
    if begin == target:
        return len(words)
    
    remain = 0
    for i in range(len(words)):
        if len(set(begin + words[i])) == len(begin) + 1:
            # target으로 변환 시 남은 리스트의 개수를 반환하므로 최소 단계를 위해서는 남은 리스트의 개수가 최대가 되어야 한다
            remain = max(remain, dfs(words[i], target, words[:i] + words[i+1:]))
        
    return remain

def solution(begin, target, words):
    answer = 0
    if target in words:
        answer = len(words) - dfs(begin, target, words)
    
    return answer