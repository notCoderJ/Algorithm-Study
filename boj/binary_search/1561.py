'''
  풀이
    한참 고민끝에 풀이 방향은 잘 잡았지만...
    마지막 처리하는 부분에서 도저히 생각이 안나서 구글링을 했다...
    그런데도 한부분에서 걸려서 한참 헤맸다 -_-
    
    풀이에 사용된 기본 알고리즘은 다음과 같다.
    1. 탑승 시간을 대상으로 이분 탐색을 수행하며, 모든 인원이 탈 수 있는 최소 시간을 구한다.
    2. 구한 최소 시간 - 1 시간(바로전 시간)에 탑승한 인원들을 구한다.
    3. 놀이기구를 하나씩 순회하며 1에서 구한 시간에 새로 탑승하는 경우 2에서 구한 인원에 1을 추가한다.
    4. 모든 인원이 탑승하면 해당 놀이기구 번호를 출력하면 된다.
    
    여기서, 탑승 인원을 계산할 때 "주어진 시간 // 놀이기구 시간 + 1"을 해줘야한다.
    +1을 해주는 이유는 나머지가 있건없건 한명을 더 탑승시킬 수 있기 때문이다.
    나머지가 있는 경우에는 당연히 탑승이 가능하다는 것을 알 수 있고,
    나머지가 0일 때는 놀이기구가 끝났을테니 바로 한명을 탑승시킬 수 있다.
    이 부분을 미처 생각하지 못해서 한~~~~~~~~~~~~~~~~~~~~참을 해멨다😇
'''

import sys
input = lambda: sys.stdin.readline().strip()
MAX = int(2 * 30 * 1e9)

def solution():
  n, m = map(int, input().split())
  rides = list(map(int, input().split()))
  if n <= m:
    print(n)
    return
  
  def ride(target):
    people = n
    for t in rides:
      people -= target // t + 1
      if people <= 0:
        return True
    return False
  
  time = -1
  left, right = 1, MAX
  while left <= right:
    mid = (left + right) // 2
    if ride(mid):
      time = mid
      right = mid - 1
    else:
      left = mid + 1

  before = sum([(time - 1) // r + 1 for r in rides])
  for i, r in enumerate(rides):
    if not time % r:
      before += 1
      if before == n:
        print(i + 1)
        return
  
if __name__ == '__main__':
  solution()