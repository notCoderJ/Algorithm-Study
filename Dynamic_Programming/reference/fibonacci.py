# 기존 재귀 방식을 이용한 피보나치 수열 알고리즘
def fibo(n):
    if n == 1 or n == 2:
        return 1
    elif n <= 0:
        return None
    return fibo(n - 1) + fibo(n - 2)

print(fibo(100)) # O(2ⁿ)의 시간 복잡도로 인해 평생 연산해도 구하지 못함.