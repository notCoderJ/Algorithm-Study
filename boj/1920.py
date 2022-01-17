'''
 풀이
  많은 수의 데이터 중 특정한 수를 찾는 문제이므로 집합이나 이진 탐색을 이용해 풀 수 있다.
'''

import sys
input = lambda: sys.stdin.readline().strip()

# 집합을 이용한 풀이
def solution():
  _ = int(input())
  nums = set(map(int, input().split()))
  _ = int(input())
  print(*[1 if i in nums else 0 for i in map(int, input().split())], sep='\n')

# 이진 탐색 풀이
def solution2():
  _ = int(input())
  nums = sorted(map(int, input().split()))
  _ = int(input())
  
  def binary(target):
    tg = int(target)
    left = 0
    right = len(nums) - 1
    
    while left <= right:
      mid = (left + right) // 2
      if nums[mid] == tg:
        return 1
      elif nums[mid] < tg:
        left = mid + 1
      else:
        right = mid - 1
    return 0
  
  print(*map(binary, input().split()), sep='\n')
  
if __name__ == '__main__':
  # solution()
  solution2()