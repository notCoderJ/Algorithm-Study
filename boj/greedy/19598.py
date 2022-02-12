'''
  풀이
    단순히 현재 회의 진행을 위한 빈 회의실이 없을 때마다 회의실을 하나씩 추가하면되는 그리디 알고리즘이다.
    먼저, 주어진 회의 일정에 대해 시작 시간 순으로 정렬한 후 회의를 하나씩 진행시킨다.
    모든 회의에 대해 종료 시간을 기록하면서 가장 빠른 종료 시간과 다음 회의 시작 시간을 비교하여 회의실 추가 여부를 결정한다.
      가장 빠른 종료 시간 <= 다음 회의 시작 시간 -> 기존 회의실을 사용한다.
      가장 빠른 종료 시간 > 다음 회의 시작 시간 -> 새로운 회의실을 1개 추가한다.
    여기서, 종료 시간을 가장 빠른 순서대로 비교하기 위해 우선순위 큐를 사용하였다.
'''

import sys
import heapq
input = lambda: sys.stdin.readline().strip()

def solution():
  answer = 0
  n = int(input())
  meetings = [tuple(map(int, input().split())) for _ in range(n)]
  meetings.sort()
  hq = []
  
  for s, e in meetings:
    if not hq or hq[0] > s:
      answer += 1
    else:
      heapq.heappop(hq)
    heapq.heappush(hq, e)

  print(answer)
  
if __name__ == '__main__':
  solution()