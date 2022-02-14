'''
  풀이
    단순히 현재 진행 중인 강의들 중 최단 종료시간과 진행할 강의의 시작시간을 비교하여
    강의실 추가 여부를 결정하면 되는 그리디 알고리즘이다.
    
    처음에는 강의 번호가 주어져 약간 혼동이 있었지만, 강의 번호는 문제에 영향을 주지 않았다.
    주어진 강의들을 시작시간 기준으로 정렬한 후 하나씩 순회하며 다음 과정을 반복하였다.
      만약 현재 진행 중인 강의들 중 최단 종료시간 <= 현재 진행할 강의의 시작 시간이면 기존 강의실을 사용한다.
      그렇지 않으면 새로운 강의실을 1개 추가하여 진행한다.
    이때, 진행하는 강의마다 종료시간을 우선순위 큐에 넣어 최단 종료시간을 구하였다.
'''

import sys
import heapq
input = lambda: sys.stdin.readline().strip()

def solution():
  n = int(input())
  lectures = [list(map(int, input().split())) for _ in range(n)]

  cnt = 0
  hq = []
  for _, s, e in sorted(lectures, key=lambda x: x[1]):
    if hq and hq[0] <= s:
      heapq.heappop(hq)
    else:
      cnt += 1
    heapq.heappush(hq, e)
    
  print(cnt)
  
if __name__ == '__main__':
  solution()