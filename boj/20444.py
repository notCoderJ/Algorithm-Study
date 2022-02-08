'''
  풀이
    색종이를 자르는 n의 최대 범위가 2^31 - 1이므로 완전탐색을 이용하면 해결할 수 없다.
    그래서 색종이를 자르는 방향을 두 방향으로 잡고 한 방향에서 자르는 횟수를 이분 탐색의 대상으로 놓고 풀이했다.
      총 자르는 횟수를 n, 한 방향에서 색종이를 자르는 횟수를 x라 하면
      색종이의 조각 수 = 색종이를 자르는 횟수 + 1이므로
      두 방향에서 색종이를 자를 경우 색종이의 조각 수 = (x + 1) * (n - x + 1)이 된다.
    따라서, 각 중간 값에 대해 위 식을 적용하여 조각이 k가 되는 값이 존재하는지 확인하면 된다.
'''

import sys
input = lambda: sys.stdin.readline().strip()

def solution():
  n, k = map(int, input().split())
  cnt = lambda x: (x + 1) * (n - x + 1)
  
  left, right = 1, n
  while left <= right:
    mid = (left + right) // 2
    piece = cnt(mid)
    if piece == k:
      print('YES')
      return
    elif piece > k:
      left = mid + 1
    else:
      right = mid - 1
  
  print('NO')

if __name__ == '__main__':
  solution()