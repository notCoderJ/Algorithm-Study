'''
  풀이
    주어진 n, m의 최대 개수가 500,000이므로 O(N^2) 알고리즘은 불가능하다.
    
    1. 딕셔너리를 이용한 풀이 - 시간 복잡도 O(N)
      a. 처음 주어지는 n개의 수를 순회하며 각 숫자의 개수를 카운팅한다.(시간복잡도 - O(N))
      b. 다음으로 주어지는 m개의 수를 순회하며 해당 숫자의 개수를 구한다.(시간복잡도 - O(M))
    
    2. 이분 탐색의 lower bound & upper bound를 이용한 풀이 - 시간 복잡도 O(NlogN) (N >= M)
      a. 처음 주어지는 n개의 수를 정렬한다. (시간복잡도 - O(NlogN))
      b. 다음으로 주어지는 m개의 수를 순회하며 이분 탐색을 이용해 해당 숫자의 개수를 구한다.(시간복잡도 - O(MlogN))
'''

import sys
from collections import Counter
from bisect import bisect_left, bisect_right

input = lambda: sys.stdin.readline().strip()

# 딕셔너리 풀이
def solution():
  _ = int(input())
  nums = Counter(map(int, input().split()))
  _ = int(input())
  print(*map(lambda x: nums[int(x)], input().split()))

# 이분탐색 풀이
def solution2():
  _ = int(input())
  nums = sorted(map(int, input().split()))
  _ = int(input())
  print(*[bisect_right(nums, n) - bisect_left(nums, n) for n in map(int, input().split())])

if __name__ == '__main__':
  solution()
  solution2()