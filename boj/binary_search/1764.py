'''
  풀이
    주어지는 데이터의 최대 개수를 고려할 때 O(N^2) 알고리즘은 불가능하다.
    1. 집합을 이용
      듣도 못한 사람의 집합을 구하고 보도 못한 사람이 해당 집합에 포함되는지 구하면 된다.
      듣도 보도 못한 사람의 수를 K(<= 500,000)라 할 때 시간 복잡도는
        - O(M) + O(KlogK) < 10,500,000
      이므로 충분히 가능하다.
  
    2. 이분 탐색
      듣도 못한 사람의 리스트를 정렬한 후 보도 못한 사람이 해당 리스트에 포함되는지 이분 탐색을 이용해 구하면 된다.
        - 초기 정렬 O(NlogN) < 10,000,000
        - 각 수의 탐색 O(logN * M * 문자열 길이) < 약 2억미만(문자열 내 탐색을 고려할 때)
      하지만, 중복 이름이 존재하지 않으므로 각 수의 탐색에서 연산 횟수는 훨씬 줄어들고 이분 탐색이 가능하다.
'''

import sys
input = lambda: sys.stdin.readline().strip()

# 집합을 이용한 풀이
def solution():
  n, m = map(int, input().split())
  dont_hear = {input() for _ in range(n)}
  answer = []
  for _ in range(m):
    name = input()
    if name in dont_hear:
      answer.append(name)
  print(len(answer), *sorted(answer), sep='\n')
  
# 이분 탐색 풀이
def solution2():
  n, m = map(int, input().split())
  dont_hear = sorted([input() for _ in range(n)])
  
  def binary(target):
    left = 0
    right = len(dont_hear) - 1
    
    while left < right:
      mid = (left + right) // 2
      if dont_hear[mid] < target:
        left = mid + 1
      else:
        right = mid
    return True if dont_hear[left] == target else False

  answer = []
  for _ in range(m):
    name = input()
    if binary(name):
      answer.append(name)

  print(len(answer), *sorted(answer), sep='\n')

if __name__ == '__main__':
  # solution()
  solution2()