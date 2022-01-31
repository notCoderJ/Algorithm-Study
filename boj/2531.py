'''
  풀이
    문제를 잘못 이해해서 시간이 꽤 걸렸다
    처음에는 쿠폰을 쓰면 하나 더 선택 가능한 줄 알고...허허허
    
    주어진 접시 개수(n)가 30,000이고 연속으로 선택하는 횟수(k)가 3,000이므로
    완전탐색을 해도 아슬아슬하게 될 것도 같지만 연산 몇 개가 더 추가된다면 불가능할 듯하다.
    그래서, 투포인터를 사용한 방법으로 풀이했다.
    회전 벨트에서 k개를 연속으로 선택하는 경우를 선형으로 보기 위해
    주어진 스시들 + 앞에서부터 k - 1개의 스시를 새로운 리스트로 정의하여 순회했다.
    (맨 마지막 1개 + 앞에서부터 k - 1개를 선택하는 것까지 포함시키면 모든 경우를 조회가능)
    
    앞에서 정의한 스시 리스트를 순회하며 연속으로 k개를 선택하고
    이전 스시 종류와 현재 선택한 스시 종류를 비교하여 최댓값으로 갱신해준다.
      이때, 선택한 스시 종류에 무료 스시가 없으면 +1을 더해 비교한다.
      (서로 다른 종류를 효율적으로 계산하기 위해 딕셔너리를 사용하였다.)
    선택한 스시가 k개면 좌측 지점의 스시를 하나 제거하고 새로운 스시를 하나 추가하며 위 과정을 반복한다.
'''

import sys
from collections import defaultdict
input = lambda: sys.stdin.readline().strip()

def solution():
  answer = -1
  n, _, k, c = map(int, input().split())
  sushi = [int(input()) for _ in range(n)]
  sushi = sushi + sushi[:k - 1]
  
  l, cnt = 0, k
  select = defaultdict(int)
  for s in sushi:
    select[s] += 1
    cnt -= 1
    if not cnt:
      answer = max(answer, len(select) + (0 if c in select else 1))
      select[sushi[l]] -= 1
      if not select[sushi[l]]:
        del(select[sushi[l]])
      cnt += 1
      l += 1

  print(answer)
  
if __name__ == "__main__":
  solution()