'''
  풀이
    코드가... 상당히 부끄럽다;;😅
    최대 구간 범위가 10 이하이므로 완전 탐색으로 모든 구간 조합을 구해도 가능하다.
    
    1. A구간이 가능한 모든 조합을 구한다.(구간 수는 1 ~ n - 1, 각 구간은 1구역 이상 포함해야하므로)
    2. A구간의 각 경우에서 bfs를 이용하여 포함된 구역들이 연결되어있는지 확인한다.
      이때, 연결되어있으면 포함된 전체 인원 수를 반환하고 아닌 경우 0을 반환해서
      각 구간에 대한 정보를 딕셔너리에 저장해둔다.(B구간이 연결되어 있는지와 B구간 인원 확인을 위함)
    3. 2에서 구한 딕셔너리를 순회하며 각 경우에서 A구간 총 인원과 B구간 총 인원을 구한다.
      두 구간 모두 총 인원이 0이 아닌 경우 둘의 차를 구하고 현재 값과 비교하여 최소값을 구한다.
'''

import sys
from collections import deque
input = lambda: sys.stdin.readline().strip()

def solution():
  answer = 1000
  n = int(input())
  people = [0] + list(map(int, input().split()))

  area = [[] for _ in range(n + 1)]
  for i in range(1, n + 1):
    cities = list(map(int, input().split()))
    if cities[0] != 0:
      area[i] = cities[1:]
      for j in cities[1:]:
        area[j].append(i)
  
  areaA = []

  def combinations(arr, start, l):
    if len(arr) == l:
      areaA.append(arr)
    
    for i in range(start, n + 1):
      combinations(arr + [i], i + 1, l)
  
  # A 구간 조합을 모두 구한다.
  for i in range(1, n):
    combinations([], 1, i)
  
  def bfs(start, cities):
    q = deque([start])
    visited = [False] * (n + 1)
    visited[start] = True
    cnt, total = 0, 0
    
    while q:
      cur = q.popleft()
      total += people[cur]
      cnt += 1
      
      for a in area[cur]:
        if not visited[a] and a in set(cities):
          q.append(a)
          visited[a] = True

    return 0 if cnt != len(cities) else total
  
  # 각 A구간이 서로 연결됬는지 확인 후 연결된 경우 총 인원 수를, 아닌 경우 0을 저장한다.
  connected = {}
  for a in areaA:
    connected[tuple(a)] = bfs(a[0], a)
  
  # A구간 총 인원이 0이 아닌 경우 B구간을 구해 연결됬는지 확인 후 차를 구한다.
  for k, v in connected.items():
    if v != 0:
      A, a_sum = set(k), v
      areaB = tuple([i for i in range(1, n + 1) if i not in A])
      b_sum = connected[areaB]
      if b_sum != 0:
        answer = min(answer, abs(a_sum - b_sum))

  return answer if answer != 1000 else -1
  
if __name__ == '__main__':
  print(solution())
