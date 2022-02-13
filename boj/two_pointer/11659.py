'''
  풀이
    n개의 수 중 i에서 j까지 구간합을 m번 구해야한다.
    i, j 범위가 1 ~ 100,000까지이고 m 또한 동일한 범위이므로
    완전 탐색을 할 경우 시간 복잡도는 O(N^2) == 100,000 * 100,000으로 불가능하다.
    
    i ~ j까지의 구간합은 sum(1 ~ j) - sum(1 ~ i - 1)와 같으므로
    주어진 n개의 수를 순회하며 각 위치에서 총 합을 구해놓고
    투포인터를 사용해 m개의 조건에 대해 각각 총 합의 두 지점 차를 구하면 된다.
'''

import sys
input = lambda: sys.stdin.readline().strip()

def solution():
  _, m = map(int, input().split())
  nums = [0]
  for i in map(int, input().split()):
    nums.append(nums[-1] + i)
  
  case = [map(int, input().split()) for _ in range(m)]
  print(*[nums[j] - nums[i - 1] for i, j in case], sep='\n')
    
if __name__ == "__main__":
  solution()