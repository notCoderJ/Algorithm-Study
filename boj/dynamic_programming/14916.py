'''
  풀이
    주어진 동전이 2, 5원으로 5원이 특정 개수의 2원을 포함할 수 없기 때문에 그리디 알고리즘으론 해결할 수 없다.
    다이나믹 프로그래밍을 사용해서 풀 수 있는데, 주어진 금액까지 바텀-업 방식으로 거슬러줄 동전의 개수를 구하면 된다.
    현재 금액을 거슬러줄 수 있는 경우에 대해 점화식을 세워보면 다음과 같다.
      현재 금액 A(X) = min(A(X-2), A(x-5)) + 1 (+1은 2원 or 5원 1개)
    
    그럼 먼저, 초기 0 ~ 5원까지 거슬러줄 동전의 개수를 정의해두고 -> [0, INF, 1, INF, 2, 1]
    (여기서, 최소 개수 계산을 위해 불가능한 경우는 INF로 처리하였다.)
    6부터 주어진 금액까지 순회하며, 위 점화식을 적용하여 메모이제이션 테이블을 완성한다.
    거스름 돈의 최소 개수를 출력할 때 INF값보다 크다면 불가능한 것이므로 -1을 출력하면 된다.
    
    ps. 이전에 풀었던 기록이 있었는데, 이전 풀이가 훨씬 난 것 같아 추가해두었다.(흠흠흠)
      주어진 금액을 5원으로 거슬러줄 수 있는 최대 5원의 개수까지 순회하면서
      각각에 대해 필요한 2원의 개수를 구하고, 5원과 2원의 개수 합이 최소가 되는 경우를 찾는 방법이다.
'''

import sys
input = lambda: sys.stdin.readline().strip()
INF = 100_001

def solution(n):
  change = [0, INF, 1, INF, 2, 1] # 0 ~ 5
  for i in range(6, n + 1):
    change.append(min(change[i - 2], change[i - 5]) + 1)
  return change[n] if change[n] < INF else -1

def old_solution(n):
  MAX, cnt = 50_001, 50_001
  
  for i in range((n // 5) + 1):
    q, r = divmod(n - 5 * i, 2)
    if r == 0:
      cnt = min(cnt, q + i)
  return cnt if cnt != MAX else -1
  
if __name__ == '__main__':
  print(solution(int(input())))
  print(old_solution(int(input())))