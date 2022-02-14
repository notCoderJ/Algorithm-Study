'''
  풀이
    1374번 문제와 거의 동일한 그리디 알고리즘 문제이다.
    풀이 방법 역시 완벽히 동일하다.
    주어진 강의들을 시작시간 기준으로 정렬한 후 하나씩 순회하며
    현재 진행 중인 강의 중 최단 종료시간과 진행할 강의의 시작시간을 비교하여
    새로운 강의실 추가여부를 결정하면 된다.
    (이때, 최단 종료시간을 구하기 위해 우선순위 큐를 사용하였다.)
'''

import sys
import heapq
input = lambda: sys.stdin.readline().strip()

def solution():
  n = int(input())
  lectures = [tuple(map(int, input().split())) for _ in range(n)]
  
  hq = []
  cnt = 0
  for s, e in sorted(lectures):
    if hq and hq[0] <= s:
      heapq.heappop(hq)
    else:
      cnt += 1
    heapq.heappush(hq, e)

  print(cnt)
  
if __name__ == '__main__':
  solution()