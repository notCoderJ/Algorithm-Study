'''
  풀이
    메모리 초과로 인해 심히 고통받았다😤
    처음 생각한 방법은 각 라인의 자리마다 (최댓값, 최솟값)을 구한 후 마지막 라인에서 최대, 최소를 알아내는 방법이었다.
    풀이 방법 자체는 틀리지 않았다고 생각했지만, 메모리 초과가 여러번 발생했다...
    주어진 메모리 제한이 4MB였고 이는 리스트로 볼 때 약 1,000,000개의 원소를 할당할 수 있는 크기라고 한다.
    맨처음 dp테이블을 n + 1개(초기값 0 추가) 생성한 후 채워나가는 방법으로 풀이한 결과 메모리 초과...
    이유가 뭐였을까 생각해봤다.
      1. 초기 입력값을 저장한 리스트 최대 크기: 3 * 100,000 = 300,000
      2. n + 1개의 행과 각 열마다 (최대, 최소)로 구성된 3개의 열을 지닌 dp테이블: 100,000 * 3 * 2 = 600,000
    total: 900,000 + for문에 사용한 enumerate 및 추가 변수 사용
    위 같은 결과로 메모리 초과가 발생했다는 생각이 들었다.
    
    그래서 2번에서 생성했던 리스트를 다음과 같이 행이 2개인 리스트로 크게 축소했다.
      이전까지 누적된 (최대, 최소값)을 지닌 행 + 현재 계산할 행
    변경 후 다시 시도한 결과 여전히 메모리 초과... 여기서 심히 멘붕이 왔다.
    리스트의 개수를 볼 때 충분하다고 생각했기에 어디가 잘못된 건지 한참을 고민했다.
    현재 상황에서 문제될 수 있는 부분은 for문에서 주어진 숫자 리스트로 생성한 enumerate라고 생각했고
    이를 단순 인덱스 리스트로 변경한 후 기존 숫자 리스트에 접근하도록 변경했다. 그 결과 메모리 초과 지옥에서 벗어날 수 있었다🎉🎉
    일반적으로 문제에서 메모리 제한이 널널했기 때문에 지금껏 enumerate를 그냥 사용해도 크게 문제될 일이 없었지만
    이번 문제같은 경우 메모리 제한이 팍팍해서 신중히 고려해야 했던 것 같다.
'''

import sys
input = lambda: sys.stdin.readline().strip()
MAX = 900001

def solution():
  answer = [-1, MAX]
  n = int(input())
  nums = [tuple(map(int, input().split())) for _ in range(n)]
  lines = [[[0, 0], [0, 0], [0, 0]]]
  pos = [-1, 0, 1]
  
  for i in range(n):
    lines.append([[-1, MAX], [-1, MAX], [-1, MAX]])
    for j in range(3):
      for k in pos:
        if 0 <= j + k < 3:
          lines[-1][j][0] = max(lines[-1][j][0], lines[0][j + k][0])
          lines[-1][j][1] = min(lines[-1][j][1], lines[0][j + k][1])
      lines[-1][j][0] += nums[i][j]
      lines[-1][j][1] += nums[i][j]
    lines.pop(0)
  
  for a, b in lines[-1]:
    answer[0], answer[1] = max(answer[0], a), min(answer[1], b)
  print(*answer)

if __name__ == "__main__":
  solution()