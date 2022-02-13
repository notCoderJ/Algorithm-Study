'''
  풀이:
    N과 M의 범위가 1 ~ 2 * 10^5이므로 완전탐색은 불가능.(시간복잡도: O(M * N))
    주어진 N개의 수를 정렬한 배열 B를 구한 후 M개의 질문을 순회하며 이분 탐색을 이용해 구하면 된다.
    (이때, 동일한 수가 여러개 있을 수 있고 그 중 처음 등장하는 수의 인덱스를 구하는 것이므로 lower bound를 구하면 된다.)
'''

import sys
input = lambda: sys.stdin.readline().strip()

# 구현(이분탐색 lower bound)
def solution():
  n, m = map(int, input().split())
  B = sorted([int(input()) for _ in range(n)])
  
  def binary(target):
    left = 0
    right = len(B) - 1
    while left < right:
      mid = (left + right) // 2
      if B[mid] < target:
        left = mid + 1
      else:
        right = mid
    print(left if B[left] == target else -1)
    
  for i in [int(input()) for _ in range(m)]:
    binary(i)

# bisect 라이브러리 이용
from bisect import bisect_left, bisect_right

def solution2():
  n, m = map(int, input().split())
  B = sorted([int(input()) for _ in range(n)])
  
  for i in [int(input()) for _ in range(m)]:
    l = bisect_left(B, i)
    r = bisect_right(B, i)
    print(l if l != r else -1)
  
if __name__ == "__main__":
  solution()
  solution2()