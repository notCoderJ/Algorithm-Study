'''
  새롭게 알게된 점
    어떤 sequence 자료형을 map을 이용해 변환 후 변수에 map형태로 저장해놓고
    이 후에 이것을 한번 풀어 이용하게 되면 이 푼 값을 따로 저장해놓지 않는한 map에 저장된 값은 사라진다.
    예를 들어
      n = map(int, "12345")가 있을 때 다음을 차례로 수행하면
      print(max(n)) # 5
      print(max(n)) # error 
'''

import sys
input = lambda: sys.stdin.readline().strip()

def solution(cnt, seq):
  if cnt == m:
    print(*seq)
    return
  
  for i in nums:
    if visited[i]:
      continue
    
    visited[i] = True
    seq[cnt] = i
    solution(cnt + 1, seq)
    visited[i] = False

if __name__ == '__main__':
  n, m = map(int, input().split())
  nums = sorted(list(map(int, input().split())))
  visited = [False] * (max(nums) + 1)
  solution(0, [0] * m)