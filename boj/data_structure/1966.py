'''
  풀이
    주어진 문서들의 우선순위를 들어온 순서와 함께 큐에 넣고
    "현재 우선순위 >= 남은 문서들 우선순위 최대값" 을 만족할 때마다 제거하면서 순서를 카운팅
    요청한 문서의 순서와 일치한 경우 해당 문서 출력 순서 반환
'''

import sys
from collections import deque
input = lambda: sys.stdin.readline().strip()

def solution(n, m, docs):
  if n == 1:
    return 1
  
  answer = 0
  q = deque([(i, doc) for i, doc in enumerate(docs)])
  
  while q:
    order, priority = q.popleft()
    if not q or priority >= max(map(lambda x: x[1], q)):
      answer += 1
      if order == m:
        return answer
    else:
      q.append((order, priority))
  
if __name__ == '__main__':
  for _ in range(int(input())):
    n, m = map(int, input().split())
    docs = list(map(int, input().split()))
    print(solution(n, m, docs))