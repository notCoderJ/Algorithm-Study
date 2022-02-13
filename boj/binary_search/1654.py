'''
  풀이:
    최대 랜선의 길이가 2^31이므로 완전 탐색 알고리즘은 불가능하다.
    조건을 만족하는 랜선의 최대 길이를 찾아야하므로 이분 탐색의 Parametric Search로 접근할 수 있다.
    주어진 랜선의 길이 중 가장 긴 랜선을 기준으로 이분탐색을 수행하며
    중간 지점의 길이마다 해당 길이로 잘랐을 때의 랜선 개수를 구하고
    구한 랜선 개수와 요구 랜선 개수를 비교하며 가장 큰 랜선의 길이를 찾으면 된다!
'''

import sys
input = lambda: sys.stdin.readline().strip()

def solution():
  answer = -1
  k, n = map(int, input().split())
  lan = [int(input()) for _ in range(k)]
  get_cnt = lambda x: sum([l // x for l in lan])
  
  left = 1
  right = max(lan)
  while left <= right:
    mid = (left + right) // 2
    if get_cnt(mid) < n:
      right = mid - 1
    else:
      left = mid + 1
      answer = max(answer, mid)

  print(answer)

if __name__ == "__main__":
  solution()