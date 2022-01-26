'''
  풀이
    n의 범위가 1 ~ 10,000이므로 완전 탐색으로 접근하면 10,000^2으로 불가능.
    
    i ~ j까지 "연속된 부분합"이 M이 되는 모든 가지 수를 찾는 문제이므로
    투포인터 알고리즘을 사용하면 된다.
    먼저, 각 지점에서의 총합을 계산한 후
    좌측, 우측 인덱스를 0부터 시작하여 두 지점의 총합 차를 구하고 m이 될 때 가지수를 1씩 증가시키면 된다.
      두 지점의 총합 차 < m인 경우 우측 지점 인덱스를 1 증가시켜 총합 차를 늘린다.
      두 지점의 총합 차 >= m인 경우 좌측 지점 인덱스를 1 증가시켜 총합 차를 줄인다.
      (이때, 두 지점의 총합 차 == m인 경우는 우측, 좌측 어떤 지점의 인덱스를 증가시켜도 이후 다시 조정되기 때문에 상관없다.)
'''

import sys
input = lambda: sys.stdin.readline().strip()

def solution():
  answer = 0
  n, m = map(int, input().split())
  nums = list(map(int, input().split()))
  sums = [0]
  for i in nums:
    sums.append(sums[-1] + i)
  
  l, r = 0, 0
  while r < n + 1:
    partial = sums[r] - sums[l]
    if partial == m:
      answer += 1
    if partial >= m:
      l += 1
    else:
      r += 1
  
  print(answer)
  
if __name__ == "__main__":
  solution()