'''
  풀이
    전체 용액의 수 범위는 2 ~ 100,000이므로 완전 탐색을 이용할 경우 100,000 * 100,000으로 불가능.
    
    용액을 혼합하여 0에 가까운 값을 구하려면 혼합한 값이 0보다 클 때는 두 용액 중 큰 값을 줄이고
    0보다 작을 때는 두 용액 중 작은 값을 키우면 된다.
    따라서, 용액들을 오름차순으로 정렬해놓고 투포인터를 사용하여 좌측과 우측 두 지점의 값을 섞어 0과 비교하며,
    0보다 클 때는 우측 지점의 값을 줄이고 0보다 작을 때는 좌측 지점의 값을 키우면서 0에 가까운 값을 구하면 된다.
'''

import sys
input = lambda: sys.stdin.readline().strip()

def solution():
  n = int(input())
  liquids = sorted(map(int, input().split()))
  
  current = int(2e9)
  lq1, lq2 = -1, -1
  l, r = 0, len(liquids) - 1
  while l < r:
    mixed = liquids[l] + liquids[r]
    if current > abs(mixed):
      current = abs(mixed)
      lq1, lq2 = l, r
    if mixed < 0:
      l += 1
    else:
      r -= 1

  print(liquids[lq1], liquids[lq2])  

if __name__ == "__main__":
  solution()