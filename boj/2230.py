'''
  풀이
    주어진 n의 범위가 1 ~ 100,000이므로 완전 탐색이 불가능.
    
    주어진 수들을 오름차 순으로 정렬한 후 좌측, 우측 시작 지점을 동일한 0번 인덱스로 잡고 투 포인터를 사용하면 된다.
    두 위치에 있는 수의 차와 M을 비교하여 M이상 일 때마다 차이의 최소값을 기록하며 다음 과정을 반복하여 탐색한다.
      수의 차 >= m 이면 차를 더 줄여도 되므로 좌측 포인터를 1 증가시킨다.
      수의 차 < m 이면 차를 더 늘려야 하므로 우측 포인터를 1 증가시킨다.
    이때, 주의할 점은 m의 범위가 0을 포함하기 때문에 좌우측 포인터들이 증가하는 조건을 각각 n보다 작을 때로 설정해주어야 한다.
'''

import sys
input = lambda: sys.stdin.readline().strip()

def solution():
  n, m = map(int, input().split())
  nums = sorted([int(input()) for _ in range(n)])
  answer = int(2e9)
  
  l, r = 0, 0
  while l < n and r < n:
    diff = abs(nums[r] - nums[l])
    if diff >= m:
      answer = min(answer, diff)
      l += 1
    else:
      r += 1

  print(answer)
  
if __name__ == "__main__":
  solution()