'''
  풀이
    음... 간단한 문제였지만, 범위가 최대 1억이라서 쉽게 접근해도 될 것 같아 시도했는데 시간초과가 나버렸다...
    처음 시도는 다음과 같았다.
    주어진 n부터 역순으로 1씩 감소시키면서 현재 숫자를 집합으로 변환하고 주어진 숫자들과 차집합을 구해
    차집합이 공집합이 되는 수를 반환했다.
    이때, 놓쳤던 부분은 숫자를 집합으로 변환할 때의 연산 횟수와 차집합을 구할 때의 연산 횟수가 될 것이다.
    예를 들어 n이 1억으로 주어지고 주어진 수가 1만 있다면
      최댓값은 11,111,111이 되어 약 9000만번 순회를 해야하는데,
      여기에 집합 연산들을 누적하면 시간 초과가 날 수 밖에 없다.
    
    그래서, 그냥 주어진 숫자들로 'n의 길이와 같은 가능한 숫자'와 'n의 길이 - 1의 길이와 같은 가능한 숫자'를
    모두 구하며 n보다 작거나 같을 때 최댓값을 갱신해주었다.
'''

import sys
input = lambda: sys.stdin.readline().strip()

def solution(n, k, nums):
  answer = -1
  
  def make_num(digit, num):
    nonlocal answer
    if digit == 0:
      if n >= int(num):
        answer = max(answer, int(num))
      return
    for i in nums:
      make_num(digit - 1, num + i)
  
  make_num(len(str(n)), '')
  make_num(len(str(n)) - 1, '')
  return answer
  
if __name__ == '__main__':
  n, k = map(int, input().split())
  nums = list(input().split())
  print(solution(n, k, nums))