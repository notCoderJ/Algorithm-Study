'''
  풀이
    구하고자 하는 것: 최대한 많은 파를 넣었을 때 남은 파의 양
    주어진 파 길이의 최대 범위: 1 ~ 1,000,000,000
    1) 파 길이의 범위를 볼 때 완전 탐색 불가능.
    2) 파닭 하나에 넣는 파의 길이를 이분 탐색의 대상으로 잡고 parametric search를 적용
      1. 1 ~ 최대 파의 길이(max(green_onions))까지 범위에서 이분탐색을 수행
      2. 중간값에 대해 각 파로 만들 수 있는 파닭 수의 합을 구한다.
      3. 2에서 구한 파닭 수와 총 주문받은 파닭 수(c)를 비교해 다음 과정을 반복 수행하며 파닭 하나에 들어가는 파의 길이를 구한다.
        3-1. 파닭 수 합 < 주문받은 파닭 수
          들어가는 파의 양을 줄여야하므로 right = mid - 1로 파닭에 들어가는 파의 길이를 줄인다.
        3-2. 파닭 수 합 >= 주문받은 파닭 수
          들어가는 파의 양을 늘려도되므로 left = mid + 1로 파닭에 들어가는 파의 길이를 늘리고 현재 파의 길이를 저장한다.
      4. 문제에서 구하고자 하는 것은 파닭을 만들고 남은 파의 양이므로 3에서 구한 최대 파의 길이를 이용해 남은 파의 길이를 구한다.
        파닭 만들고 남은 파 길이 = 전체 파 길이 - (파닭 하나에 들어가는 최대 파 길이 * 파닭 수)
'''

import sys
input = lambda: sys.stdin.readline().strip()

def solution():
  s, c = map(int, input().split())
  green_onions = [int(input()) for _ in range(s)]
  cnt = lambda x: sum([g // x for g in green_onions])
  
  answer = -1
  left, right = 1, max(green_onions)
  while left <= right:
    mid = (left + right) // 2
    if cnt(mid) < c:
      right = mid - 1
    else:
      left = mid + 1
      answer = mid

  print(sum(green_onions) - answer * c)

if __name__ == '__main__':
  solution()