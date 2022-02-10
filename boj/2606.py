'''
  풀이
    처음 문제를 봤을 때 분리된 트리 형태를 보고 서로소 집합 알고리즘이 떠올라서 해당 알고리즘으로 풀이를 했고, DFS나 BFS를 이용한 그래프 탐색으로도 가능하다고 생각하여 각 방법으로 풀어보았다.
    
    1. 서로소 집합 알고리즘
      먼저, 루트 컴퓨터를 해당 컴퓨터에 연결된 가장 낮은 번호의 컴퓨터라고 하고 현재 컴퓨터 자신의 번호를 루트 컴퓨터로 갖는 테이블을 정의해준다.
      그 다음 주어진 컴퓨터들을 연결하기 위한 union연산과 각 컴퓨터에 연결된 루트 컴퓨터를 찾기 위한 find연산을 정의한다.
      
      이제, 주어진 연결 정보에 대해 union연산을 수행하며 다음과 같이 각 컴퓨터의 루트 컴퓨터를 갱신해주는 작업을 수행하면 된다.
        1. 두 컴퓨터의 루트 컴퓨터 번호를 구한다.
        2. 두 루트 컴퓨터 번호를 비교하여 더 낮은 번호로 테이블을 갱신한다.
      모든 과정이 끝난 후 각 컴퓨터에 대해 루트 컴퓨터를 찾아 해당 번호가 1이 되는 컴퓨터들을 카운팅하면 된다.
      
      여기서, 마지막에 각 컴퓨터에서 루트 컴퓨터를 찾는 과정을 잊어버려 조금 헤맸다...
      예를 들어 연결 정보가 (1, 2), (3, 7), (7, 1)와 같이 주어질 때 테이블을 갱신한 결과를 보면
        node 1 2 3 7
        root 1 1 1 3
      위와 같이 되어 7번 컴퓨터의 루트 컴퓨터를 찾기 위해 테이블을 탐색해줘야 한다.
      
    2. DFS
      일반적인 DFS 풀이와 동일하다.
      주어진 연결 정보를 이용해 그래프를 만들고, 1번 노드를 시작으로 방문한 노드들을 방문 처리 후
      카운팅하며 방문하지 않은 모든 연결된 노드들을 탐색해주면 된다.
    
    3. BFS
      탐색 방법은 DFS 풀이와 유사하고 큐를 사용하여 방문할 노드들을 추가하며 탐색하는 차이가 있다.
'''

n = int(input())
m = int(input())

# 1. 서로소 집합 풀이
  
def solution():
  graph = [list(map(int, input().split())) for _ in range(m)]
  parents = [i for i in range(n + 1)]
  
  def find(node):
    if parents[node] != node:
      parents[node] = find(parents[node])
    return parents[node]

  def union(n1, n2):
    r1 = find(n1)
    r2 = find(n2)
    if r1 > r2:
      parents[r1] = r2
    else:
      parents[r2] = r1

  for n1, n2 in graph:
    union(n1, n2)
    
  for i in range(n + 1):
    parents[i] = find(i)
    
  print(parents.count(1) - 1)


# 2. DFS 풀이
def solution2():
  graph = [[] for _ in range(n + 1)]
  visited = [False] * (n + 1)
  
  for _ in range(m):
    c1, c2 = map(int, input().split())
    graph[c1].append(c2)
    graph[c2].append(c1)
  
  def dfs(node):
    answer = 0
    visited[node] = True
    
    for i in graph[node]:
      if not visited[i]:
        answer += dfs(i) + 1
    return answer
  
  print(dfs(1))


# 3. BFS 풀이
from collections import deque

def solution3():
  answer = 0
  graph = [[] for _ in range(n + 1)]
  visited = [False] * (n + 1)
  
  for _ in range(m):
    c1, c2 = map(int, input().split())
    graph[c1].append(c2)
    graph[c2].append(c1)
  
  dq = deque([1])
  visited[1] = True
  while dq:
    node = dq.popleft()
    
    for i in graph[node]:
      if not visited[i]:
        answer += 1
        visited[i] = True
        dq.append(i)

  print(answer)
  

if __name__ == '__main__':
  # solution()
  # solution2()
  solution3()
  