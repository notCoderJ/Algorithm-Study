'''
  풀이
    단순히 문제에 주어진 설명을 그대로 따르면 된다
    에라토스테네스의 체를 이용하여 숫자들을 지우며 카운트한다.
    현재 카운트가 k와 일치하면 현재 숫자를 출력한다.
'''

import sys
input = lambda: sys.stdin.readline().strip()

def solution(n, k):
  cnt = 0
  primes = [True] * (n + 1)
  for i in range(2, n + 1):
    for j in range(i, n + 1, i):
      cnt += [0, 1][primes[j]]
      if cnt == k:
        return j
      primes[j] = False

if __name__ == '__main__':
  n, k = map(int, input().split())
  print(solution(n, k))