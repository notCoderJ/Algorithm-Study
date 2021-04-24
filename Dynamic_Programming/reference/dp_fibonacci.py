# 다이나믹 프로그래밍을 이용한 피보나치 수열 알고리즘

# 메모이제이션 기법을 적용한 재귀 형태의 Top-Down 방식(함수 호출 오버헤드 발생)
# 재귀 함수 방식을 사용하면 Call Stack이 초과되는 경우가 발생할 수도 있다.
# 이때 sys 라이브러리의 setrecursionlimit() 함수를 사용하면 재귀 제한을 해제할 수 있다.
memo = [0] * 101

def fibo(n):
    if n == 1 or n == 2:
        return 1
    elif n <= 0:
        return None

    if memo[n] != 0:
        return memo[n]

    memo[n] = fibo(n - 1) + fibo(n - 2)
    return memo[n]

# print(fibo(100))

# 반복문을 이용한 Bottom-Up 방식(함수 호출 오버헤드 발생 X)
memo[1] = 1
memo[2] = 1
n = 100

for i in range(3, n + 1):
    memo[i] = memo[i - 1] + memo[i - 2]

print(memo[n])