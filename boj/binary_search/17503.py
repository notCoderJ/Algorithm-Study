'''
  풀이
    구하고자 하는 것: 선호도를 만족하며 n개의 맥주를 먹을 수 있는 최소 간 수치
    주어진 도수 레벨 최대 범위: 1 ~ 2^31 - 1
    1) 도수 레벨 범위를 볼 때 완전 탐색 불가능.
    2) 간 수치를 이분 탐색의 대상으로 잡고 parametric search를 적용
      1. 1 ~ 최대 도수까지 범위에서 이분탐색을 수행
      2. 중간값에 대해 도수를 만족하며 n일간 마신 선호도 합을 구한다.
        (이때, 마실 수 있는 맥주가 n일보다 적다면 -1을 반환하여 간 수치를 올려주어야 한다.)
      3. 2에서 구한 선호도 합과 채워야하는 선호도 합(m)을 비교해 다음 과정을 반복 수행하며 간 수치를 구한다.
        3-1. 선호도 합 < 채워야하는 선호도 합
          간 수치를 늘려야하므로 left = mid + 1로 간 수치를 강화한다.
        3-2. 선호도 합 >= 채워야하는 선호도 합
          간 수치를 줄여도되므로 right = mid - 1로 간 수치를 낮추고 현재 간 수치를 저장한다.
          
    이 문제는 이분 탐색 외에도 우선순위 큐를 이용하여 풀 수 있었다.
    먼저, 왜 가능한지 생각해보자.
    어떤 맥주를 마시기 위해 최소로 만족해야하는 간 수치는 그 맥주의 도수이다.
    즉, 선호도 m을 만족하는 n개의 맥주를 마시기 위한 최소 간 수치는 n개의 맥주 중 최대 도수와 같다.
    따라서, 도수가 낮은 순으로 n개의 맥주 선호도를 힙에 넣은 후 채워야하는 선호도(m)을 만족하지 않았을 때마다
    선호도가 낮은 순으로 하나씩 힙에서 빼고 새로운 맥주의 선호도를 힙에 추가한다.
    위 과정을 반복하다가 조건을 만족했을 떄 현재 도수를 출력하면 된다.
    
    두 알고리즘의 성능을 비교해보자.
    먼저, 이분 탐색의 경우 탐색마다 선호도 합을 구하는 과정이 반복되므로
      시간 복잡도를 계산하면 O(KlogC)로 약 200,000 * log2^31 = 6,200,000
    다음으로, 우선순위 큐를 이용한 풀이의 시간 복잡도를 계산하면
      K개의 맥주에 대해 우선순위 큐에 한번씩 넣고뺴고 한다면(우선순위 큐에 n개의 맥주는 유지)
      약 O((k - n + 1)logK)로 200,000 * log200,000 = 3,600,000
    우선순위 큐 알고리즘이 훨씬 빠르다는 것을 알 수 있다. 실제로 결과도 약 4배정도 속도 차이가 나왔다.
'''

import sys
input = lambda: sys.stdin.readline().strip()

# 이분 탐색 풀이
def solution():
  answer = -1
  n, m, k = map(int, input().split())
  beers = sorted([list(map(int, input().split())) for _ in range(k)], reverse=True)
  
  def cnt(target):
    day = n
    preference = 0
    for b in beers:
      if b[1] <= target:
        day -= 1
        preference += b[0]
        if not day:
          return preference
    return -1
  
  left, right = 1, 2 ** 31
  while left <= right:
    mid = (left + right) // 2
    if cnt(mid) < m:
      left = mid + 1
    else:
      right = mid - 1
      answer = mid
  print(answer)
  
# 우선순위 큐 풀이
import heapq

def solution2():
  n, m, k = map(int, input().split())
  beers = sorted([list(map(int, input().split())) for _ in range(k)], key=lambda x: x[1])

  hq = []
  preference = 0
  for beer in beers:
    heapq.heappush(hq, beer[0])
    preference += beer[0]
    day = len(hq)
    
    if preference >= m and day == n:
      print(beer[1])
      return
    elif preference < m and day >= n:
      preference -= heapq.heappop(hq)

  print(-1)

if __name__ == '__main__':
  solution()
  solution2()