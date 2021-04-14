# 피보나치 수열로 비교한 다이나믹 프로그래밍 알고리즘

# 기존 재귀 방식
def fibo(n):
    if n == 1 or n == 2:
        return 1
    elif n <= 0:
        return None
    return fibo(n - 1) + fibo(n - 2)

# print(fibo(100)) # O(2^n)의 시간 복잡도로 인해 평생 연산해도 구하지 못함.

# 메모이제이션 기법을 적용한 재귀 방식(탑다운 다이나믹 프로그래밍, 함수 호출 오버헤드 O)
memo = [0] * 101

def memo_fibo(n):
    if n == 1 or n == 2:
        return 1
    elif n <= 0:
        return None

    if memo[n] != 0:
        return memo[n]

    memo[n] = memo_fibo(n - 1) + memo_fibo(n - 2)
    return memo[n]

# print(memo_fibo(100))

# 반복문을 이용한 방식(보텀업 다이나믹 프로그래밍, 함수 호출 오버헤드 X)
memo[1] = 1
memo[2] = 1
n = 100

for i in range(3, n + 1):
    memo[i] = memo[i - 1] + memo[i - 2]

print(memo[n])