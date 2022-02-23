'''
  풀이
    방향성만 잘 잡으면 그렇게 어려운 문제는 아닌 것 같았다.
    하지만, 처음에 방향성을 어떻게 잡아야할지 몰라 고민을 많이 했었다.
    문제가 그래프 유형으로 분류되어 있다는 것을 몰랐다면 아마도 많이 헤맸을 것이다...
    
    먼저, 문제에서 주어진 수들의 비교를 다음 2종류의 그래프로 생각해보자.
      1. 자신보다 작은 수를 자식 노드로 갖는 그래프
      2. 자신보다 큰 수를 자식 노드로 갖는 그래프

    예를 들어 n과 비교 관계가 다음과 같이 주어졌다고 가정하고
      n = 5, m = 4
      1 2, 3 4, 3 5, 4 5
    위 각 그래프를 인접 리스트로 표현해보면
    1번 그래프는
      1 - 2
      2 - X
      3 - 4, 5
      4 - 5
      5 - x
    가 될 것이고
    
    2번 그래프는
      1 - x
      2 - 1
      3 - x
      4 - 3
      5 - 3, 4
    가 될 것이다.
    
    이때, 3번이 가능한 등수의 최댓값과 최솟값을 구한다고 하면
    최댓값은 n개 중 3번보다 큰 수가 몇개 존재하는지 알면 구할 수 있고,
    최솟값은 n개 중 3번보다 작은 수가 몇개 존재하는지 알면 구할 수 있다.
    즉, dfs나 bfs를 사용하여 위 각 그래프들을 탐색하며 연결된 자식 노드들의 수를 카운트해주면
    원하는 최대 등수와 최소 등수를 구할 수 있다.
    
    3번의 경우 다음과 같다.
    최댓값 -> 2번 그래프 탐색시 3번보다 큰 자식노드가 없으므로 최댓값은 1이 된다.
    최솟값 -> 1번 그래프 탐색시 3번보다 작은 자식노드가 4, 5 2개 존재하므로(4번의 자식노드도 5이므로) 최솟값은 3이 된다.
'''

import sys
input = lambda: sys.stdin.readline().strip()
MIN, MAX = 0, 1

def solution():
  n, m, x = map(int, input().split())
  graph = [[[] for _ in range(n + 1)] for _ in range(2)]
  for _ in range(m):
    a, b = map(int, input().split())
    graph[MIN][a].append(b)
    graph[MAX][b].append(a)
  
  visited = [[False] * (n + 1) for _ in range(2)]
  
  def dfs(start, type):
    visited[type][start] = True
    cnt = 0
    for i in graph[type][start]:
      if not visited[type][i]:
        cnt += dfs(i, type) + 1
    return cnt
    
  print(dfs(x, MAX) + 1, n - dfs(x, MIN))
  
if __name__ == '__main__':
  solution()
