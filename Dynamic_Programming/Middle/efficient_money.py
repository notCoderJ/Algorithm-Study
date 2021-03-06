# n종류의 화폐를 사용해 가치 합이 M이 되도록 할 때 최소 개수?
# 조건 :
#   1. 각 화폐의 사용 개수 제한은 없다.
#   2. 사용 화폐의 구성이 같으면 순서가 달라도 같은 경우로 간주한다.

# 풀이 전략
'''
    m = 6이고 3개의 화폐 종류 [1, 3, 4]가 있다고 가정하고
    각 화폐 종류에 따라 최소 개수를 반환하는 함수 f의 호출을 살펴보면
    1일 때 -> f(6) = f(5) + 1
    3일 때 -> f(6) = f(3) + 1
    4일 때 -> f(6) = f(2) + 1
    이므로 f(6) = min({f(5) + 1}, {f(3) + 1}, {f(2) + 1})이 된다.

    이를 일반화하면 가치가 m일 때 화폐의 종류 k에서의 최소 개수는 f(m) = f(m-k) + 1이다.
    f(m)의 최소값은 현재 f(m)과 해당 화폐 종류에서의 f(m)값을 계속 비교하면 된다.
    따라서, 해당 문제의 점화식은 a(m) = min(a(m), a(m-k) + 1)이 된다.
'''

n, m = map(int, input().split())
weight = [int(input()) for _ in range(n)]

cnt = [10001] * (m + 1) # m이 1 ~ 10000 범위이므로 최대 가능한 개수보다 큰 값으로 초기화
cnt[0] = 0 # 0의 가치를 만드는 개수는 0

for i in weight: # 화폐 종류별로 최소 개수를 계산한다
    for j in range(i, m + 1):
        if cnt[j - i] != 10001: # 이전 가치를 만들 수 있는 경우
            # 현재 개수와 해당 화폐 종류에서의 최소 개수를 비교한다
            cnt[j] = min(cnt[j], cnt[j - i] + 1)

if cnt[m] == 10001: # 해당 가치를 만들 수 있는 화폐가 없으면 -1을 출력한다
    print(-1)
else:
    print(cnt[m])