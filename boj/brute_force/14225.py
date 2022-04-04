'''
  풀이
    최대 수열의 크기가 20 이하이므로 완전 탐색이 가능하다.
    (각 숫자를 포함할지 말지로 나누면 총 2^20 = 1,048,576이므로)
    1. 각 자리의 숫자를 저장할 리스트를 "전체 수열 합 + 1" 크기로 생성한다.
    2. 0 ~ n - 1번까지 수열의 각 자리 숫자를 포함할 때와 안할 때로 나누어 1번 리스트에 값을 저장하며 각각 재귀함수를 반복한다.
    3. 현재 자리 수가 n이 되면 포함된 숫자들의 합을 구해 해당 값과 동일한 answer의 인덱스 값을 True로 변경한다.
    4. answer 값을 순회하며 False로 남아있는 인덱스 값을 반환한다.
    (만약 없다면 answer의 길이를 출력한다, 그 이유는 모두 True이므로 가장 작은 수는 전체 수열합 + 1이다.)
'''

import sys
input = lambda: sys.stdin.readline().strip()

def solution(n, s):
  answer = [False] * (sum(s) + 1)
  nums = [0] * n
  
  def brute_force(cnt):
    if cnt == n:
      answer[sum(nums)] = True
      return
    
    nums[cnt] = 0
    brute_force(cnt + 1)
    nums[cnt] = s[cnt]
    brute_force(cnt + 1)
  
  brute_force(0)
  
  for i, v in enumerate(answer):
    if not v:
      return i

  return len(answer)
  
  
if __name__ == '__main__':
  n = int(input())
  s = list(map(int, input().split()))
  print(solution(n, s))