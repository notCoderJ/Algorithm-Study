'''
  풀이
    666을 포함한 수 6,660,000 ~ 6,669,999는 총 10,000개이고
    0부터 6,669,999까지 반복해도 연산 횟수가 충분히 적으므로 완전탐색이 가능하다.
    
    단순히 666부터 시작해서 666이 포함된 수를 하나씩 카운트하며 해당하는 숫자를 출력하면 된다.
'''

import sys
input = lambda: sys.stdin.readline().strip()

def solution(n):
  for i in range(666, 6670000):
    n -= 1 if '666' in str(i) else 0
    if n == 0:
      return i
  
if __name__ == '__main__':
  print(solution(int(input())))