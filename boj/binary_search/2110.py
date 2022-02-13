'''
  풀이
    공유기를 설치할 수 있는 최대 범위는 0 ~ 1,000,000,000이므로 완전 탐색 불가능.
    구하고자하는 것은 공유기 간 거리의 최대 값이므로
    공유기 간 거리 중 최소 거리를 이분 탐색 대상으로 잡고
    parametric search를 이용해 탐색하며 주어진 설치 개수를 넘었을 때의
    값 중 최대 값을 구하면 된다.
'''

import sys

input = lambda: sys.stdin.readline().strip()

def solution():
  answer = -1
  n, c = map(int, input().split())
  houses = sorted([int(input()) for _ in range(n)])
  
  def set_wifi(d):
    cnt = 0
    prev = -int(1e9)
    for h in houses:
      if h - prev >= d:
        cnt += 1
        prev = h
    return cnt
  
  left = 0
  right = max(houses)
  while left <= right:
    mid = (left + right) // 2
    if set_wifi(mid) < c:
      right = mid - 1
    else:
      answer = mid
      left = mid + 1
  print(answer)

if __name__ == '__main__':
  solution()