# My code
# dynamic programming version - time complexity : O(N) 

def solution(n):
    answer = ''
    dp = ['' for _ in range(n + 1)]
    trans = ['4', '1', '2']
    
    for i in range(1, n + 1):
        q, r = divmod(i, 3)
        if r == 0:
            dp[i] += dp[q - 1]
        else:
            dp[i] += dp[q]
        dp[i] += trans[i % 3]
    
    answer = dp[n]
    
    return answer