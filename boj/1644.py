'''
  풀이
    주어진 n의 범위가 1 ~ 4,000,000이기 때문에 이 범위 내 소수의 부분합을 완전 탐색으로 구하는 것은 불가능.
    
    "연속된 소수의 부분합"이 n을 만족하는 경우의 수를 구하는 문제이므로 투포인터 알고리즘을 사용하면 된다.
    그럼 먼저 주어진 n까지 범위 내 소수들을 모두 구해야하는데, n의 범위가 4,000,000까지이므로
    완전 탐색 방식으로 소수를 구하는 것 역시 불가능하다.
    따라서, 정해진 수까지 범위 내 소수들을 빠르게 구할 수 있는 "에라토스테네스의 체"를 사용하여 소수를 구하면 된다.
    이것이 가능한 이유를 살펴보자. 먼저, 2부터 시작하여 4,000,000까지 2의 배수를 제거하면 절반의 수가 제거되고
    그 다음 3의 배수를 제거하면 약 700,000개의 수가 제거된다. 이 과정의 반복은 약 O(NloglogN)의 시간 복잡도를 갖는다고 할 수 있다.
    
    이제, 에라토스테네스의 체를 이용하여 주어진 n까지 범위 내 소수들을 모두 구하고 각 지점에서의 총합을 구한다.
    그 후 좌측, 우측 인덱스를 0부터 시작하여 두 지점의 총합 차를 구하고 n이 될 때 가지수를 1씩 증가시키면 된다.
      두 지점의 총합 차 <= n인 경우 우측 지점 인덱스를 1 증가시켜 총합 차를 늘린다.
      두 지점의 총합 차 > n인 경우 좌측 지점 인덱스를 1 증가시켜 총합 차를 줄인다.
      (이때, 두 지점의 총합 차 == n인 경우는 우측, 좌측 어떤 지점의 인덱스를 증가시켜도 이후 다시 조정되기 때문에 상관없다.)
    
    위 알고리즘의 시간 복잡도를 계산해보면 에라토스테네스의 체 O(NloglogN) + 투포인터 O(N)이므로
    시간 복잡도는 O(NloglogN) ~= 16,000,000로 충분히 가능하다는 것을 알 수 있다.
'''

import sys
input = lambda: sys.stdin.readline().strip()

def get_prime(last):
  primes = [True] * (last + 1)
  primes[0], primes[1] = False, False

  for i in range(2, last + 1):
    if primes[i]:
      for j in range(i + i, last + 1, i):
        primes[j] = False
  return [i for i, p in enumerate(primes) if p]

def solution():
  answer = 0
  n = int(input())
  primes = get_prime(n)
  sums = [0]
  for i in primes:
    sums.append(sums[-1] + i)
  
  l, r = 0, 0
  while r < len(sums):
    partial = sums[r] - sums[l]
    if partial == n:
      answer += 1
    if partial > n:
      l += 1
    else:
      r += 1

  print(answer)
  
if __name__ == "__main__":
  solution()