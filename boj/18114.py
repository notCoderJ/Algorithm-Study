'''
  풀이
    주어진 물건의 개수 범위가 1 ~ 5,000이므로 완전 탐색을 할 경우 5,000^3의 시간 복잡도가 되어 불가능.
    먼저, 이분탐색으로 접근하여 조건별로 쪼개어 생각해보았다.
      물건 1개일 때 시간 복잡도는 O(logN)
      물건 2개일 때 물건 1개를 먼저 선택하고 나머지 1개를 이분탐색하면 시간 복잡도는 약 O(NlogN) (같은 물건이 중복되지 않으므로 더 작다)
      물건 3개일 때 물건 2개를 먼저 선택(O(N^2))하고 나머지 1개를 이분탐색하면 시간 복잡도는 약 O(N^2logN) (상동)
    이분탐색 이용 시 총 시간 복잡도는 O(N^2logN)으로 볼 수 있다.
    하지만 N = 5,000이라면 5,000^2 * log5,000로 약 300,000,000이 되어 불가능할 것 같다.(실제론 이것보단 적겠지만...)
    (아마 다른 방법으로 이분탐색을 할 수 있을 것 같지만 도저히 생각이 나지 않는다.)
    
    그래서, 다른 방법으로 집합을 이용한 방법을 생각해보았다.
      물건 1개일 때는 그냥 반복문으로 돌려서 확인하면 시간 복잡도는 O(N) == 5,000
      물건 2개일 때는 이중 반복문으로 2개의 수를 선택 후 합해서 주어진 무게와 일치하는 지 확인하면 시간 복잡도는 O(N^2) == 5,000^2
      물건 3개일 때는 이중 반복문으로 2개의 수를 선택한 후 합한 값을 총 무게에서 뺀 값이 존재하는 지 확인하면 시간 복잡도는 약 O(N^2) == 5,000^2
    즉, O(N^2)의 시간 복잡도로 주어진 데이터 양을 볼 때 가능하다.
    그럼에도 불구하고 파이썬으로는 계속 시간 초과로 통과되지 않았다... 끝내 파이파이로 하여 통과할 수 있었다.
    이 문제의 경우 파이썬으로 통과하려면 다른 시각에서 생각해보거나 더 성능이 좋은 알고리즘으로 구현해야될 듯 싶다.
    (다른 알고리즘 연습을 한 후 다시 돌아와서 풀어보기로...)
'''

import sys
input = lambda: sys.stdin.readline().strip()

def solution():
  _, c = map(int, input().split())
  weights = sorted((map(int, input().split())))

  # 1개
  for w in weights:
    if w == c:
      print(1)
      return
  
  # 2개
  for i in range(len(weights)):
    for j in range(i + 1, len(weights)):
      if weights[i] + weights[j] == c:
        print(1)
        return

  # 3개
  w_set = set(weights)
  for i in range(len(weights)):
    for j in range(i + 1, len(weights)):
      w = c - (weights[i] + weights[j])
      if w in w_set and w != weights[i] and w != weights[j]:
        print(1)
        return
  
  print(0)
  
if __name__ == "__main__":
  solution()