'''
  풀이:
    주어진 수열의 길이가 최대 9이므로 연산자의 수는 최대 8개
    ' ', '+', '-' 3가지 연산자로 8개를 조합하면 총 3^8 = 6,561개
    각 케이스에서 연산을 수행하면 3^8 * 약 최대 9(for문 반복횟수만 고려) = 59,049번
    따라서, 완전 탐색으로 충분히 가능한 연산 횟수

    매번 ' ', '+', '-' 연산자 중 1개를 선택하며 n-1번 반복하여 연산식을 구함
    n-1번째에 구한 연산식을 계산하여 값이 0이 되는지 확인하고 0이면 해당 연산식을 출력
'''

import sys
input = lambda: sys.stdin.readline().strip()

def solution(n):
  exp = ['' for _ in range(2 * n - 1)]
  for i in range(n):
    exp[2 * i] = str(i + 1)
    
  def calc(target):
    result = 0
    _plus = target.replace(' ', '').split('+')
    for i in _plus:
      if '-' in i:
        _minus = i.split('-')
        result += int(_minus[0])
        for j in _minus[1:]:
          result -= int(j)
      else:
        result += int(i)
    return result

  def check_zero(cnt):
    if cnt == n - 1:
      target = ''.join(exp)
      if calc(target) == 0:
        print(target)
      return
    
    for op in [' ', '+', '-']:
      exp[2 * cnt + 1] = op
      check_zero(cnt + 1)
  
  check_zero(0)
  
if __name__ == '__main__':
  for _ in range(int(input())):
    solution(int(input()))
    print()