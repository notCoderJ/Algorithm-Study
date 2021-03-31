# N개의 원소를 가진 배열 A, B에서 원소를 K번 서로 바꾸었을 때
# 배열 A의 모든 원소들의 합이 최대가 되도록 해라.

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort() # 배열 A를 오름차 정렬한다
b.sort(reverse=True) # 배열 B를 내림차 정렬한다

for i in range(k):
    # 배열 A의 가장 작은 값과 배열 B의 가장 큰 값을 순차적으로 비교하며
    # A의 값이 B의 값보다 작을 때만 서로 교환한다
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else: # 교환할 값이 없는 경우 종료한다
        break

print(sum(a))