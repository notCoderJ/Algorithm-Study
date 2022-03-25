'''
  풀이
    총 123,456개의 방에 모두 몬스터가 있고, 모든 몬스터의 체력과 공격력은 1,000,000이라고 가정하면
    용사의 공격력이 1일 때 미션을 클리어하려면 용사의 최대 최력은 123,456 * 1,000,000 * 1,000,000이 되어야하므로
    완전탐색으로는 시간 초과로 통과할 수 없다.
    
    따라서, 용사의 최대 체력을 1 ~ 123,456 * 1,000,000 * 1,000,000 사이의 범위로 놓고 이분 탐색의 Parametric Search를 적용하면 된다.
    매 중간 값(용사의 최대 체력)에 대해 현재 주어진 던전 정보를 가지고 미션을 클리어할 수 있는지 확인하며 용사의 최대 체력의 최솟값을 구한다.
      t가 1인 경우 몬스터이므로 "(몬스터 체력 // 용사 공격력) * 몬스터 공격력"만큼 용사의 현재 체력에서 깍는다.
        이때, 주의할 점은 몬스터 체력이 용사 공격력으로 나누어떨어지면 마지막 한대는 맞지 않으므로 이 경우는 몬스터 공격력을 한 번 제외시켜준다.
      t가 2인 경우 포션이므로 주어진 공격력만큼 용사의 공격력에 더해주고 용사의 현재 체력을 min(용사 최대 체력, 용사 현재 체력 + 주어진 체력)으로 갱신해준다.
'''

import sys

input = lambda: sys.stdin.readline().strip()
MAX_HP = 123_456 * 1_000_000 * 1_000_000

def solution():
  N, Hatk = map(int, input().split())
  mission = [list(map(int, input().split())) for _ in range(N)]

  def clear_mission(max_hp):
    cur_atk, cur_hp = Hatk, max_hp
    for t, a, h in mission:
      if t == 1:
        q, r = divmod(h, cur_atk)
        # 나머지가 없는 경우 몬스터가 먼저 죽기 때문에 한대를 제외한다.
        cur_hp -= q * a + [0, -a][r == 0]
        if cur_hp <= 0:
          return False
      else:
        cur_atk += a
        cur_hp = min(max_hp, cur_hp + h)
    return True
  
  answer = -1
  left, right = 1, MAX_HP
  while left <= right:
    max_hp = (left + right) // 2
    if clear_mission(max_hp):
      answer = max_hp
      right = max_hp - 1
    else:
      left = max_hp + 1
  
  print(answer)
  
if __name__ == '__main__':
  solution()