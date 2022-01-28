'''
  풀이
    문제의 골롱 수열을 이해하지 못해 1차 좌절
    검색 후 알게 되었지만 풀이가 막막해 2차 좌절
    너무 힘들었던 문제였다... 투포인터로 어떻게 풀지 감이 안와 DP풀이를 참고해 풀었다...
    
    먼저, 골롱 수열이 무엇인지 이해할 필요가 있다.
    골롱 수열은 단조증가 형태를 띈다고 하는데, 예를 들어 k = 1일 때 f(1) = 2라고 하면
      1 2 3 ...
      2 1 <- 1이 2번 나오면 k = 2일 때 f(2) = 1이 되어 f(k) 값이 감소하게 된다.
    따라서, 골롱 수열의 형태는 다음과 같은 유일한 형태를 지닌다.
      1 2 3 4 5 6 7 8 9 ...
      1 2 2 3 3 4 4 4 5 ...
    여기서, 새로운 값이 시작되는 인덱스를 기준으로 생각해보면
      1이 시작되는 인덱스 1의 f(1) = 1이 반복되는 횟수는 f(f(1)) = 1로 "2가 시작되는 인덱스는 1 + f(f(1)) = 2"
      2가 시작되는 인덱스 2의 f(2) = 2가 반복되는 횟수는 f(f(2)) = 2로 "3이 시작되는 인덱스는 2 + f(f(2)) = 4"
      3이 시작되는 인덱스 4의 f(4) = 3이 반복되는 횟수가 f(f(4)) = 2로 "4가 시작되는 인덱스는 4 + f(f(4)) = 6"
      ...
    위로부터 다음 새로운 값이 시작되는 인덱스 k는 i + f(f(i))가 성립함을 알 수 있고(i는 이전 값이 시작됐던 인덱스)
    k > n이 될 때 f(k) 이전 값인 f(k) - 1이 구하고자 하는 값이 된다.
    
    그러므로, k > n이 될 때까지 1부터 각 인덱스 i에 대해 f(i) 값을 구하면 되는데, 다음과 같이 생각해볼 수 있다.
      1 2 3 4 5 6 ...
      1 2 2 3 3 4 ...
    예를들어, 인덱스 4에서 f(4)값은 바로 이전 값 f(3)이 반복되는 횟수 f(f(3)) = 2만큼 인덱스 4에서 좌측으로 이동시키고
    그 위치의 f(2)값에 1을 더한 값과 같다.

    즉, 구하고자 하는 값 f(x)는 이전 값 f(x-1)이 반복되는 횟수만큼 인덱스 x에서 뺀 후 해당 위치의 f값에 1을 더한 값이 된다.
      f(x) = 1 + f(x - f(f(x-1)))
    만약 그 위치값이 f(x-1) - 1이라면 f(x-1)의 반복 횟수를 채우지 못했으므로 f(x) = f(x-1) = f(x-1) - 1 + 1이 성립
    그 위치값이 f(x-1)이라면 f(x-1)의 반복 횟수를 채웠으므로 f(x) = f(x-1) + 1이 되어 두 조건 모두 성립함을 알 수 있다.
    
    따라서, 위 점화식 f(x) = 1 + f(x - f(f(x-1)))을 이용하여 2부터 f(x)값을 구하면서
    새로운 값이 시작되는 인덱스 k > n이 될 때 마지막 f(x)를 구한 인덱스 값을 출력하면 된다.
'''

import sys
input = lambda: sys.stdin.readline().strip()

def solution():
  n = int(input())
  st = [0, 1]
  current = 2
  for i in range(2, n + 1):
    st.append(1 + st[i - st[st[i - 1]]])
    current += st[-1]
    if current > n:
      break

  print(len(st) - 1)
  
if __name__ == "__main__":
  solution()