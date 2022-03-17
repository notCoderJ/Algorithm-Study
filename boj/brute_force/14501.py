'''
  풀이
    날짜별로 경우의 수를 따져보면 해당 날짜에 상담을 할 경우와 하지 않을 경우 2가지가 존재한다.
    최대 15일까지 주어지므로 최대 연산 횟수는 2^15 = 32,768이고 충분히 완전 탐색으로 풀 수 있다.
    
    재귀함수를 이용해 해당하는 날에 상담할 경우와 하지 않을 경우 각각 호출하고
    퇴사일이 되었을 때 최대 수익을 비교하여 구하면 된다.
'''

import sys 
sys.setrecursionlimit(100000000)

def solution():
  n = int(input())
  profits = [(0, 0)]
  for _ in range(n):
    profits.append(tuple(map(int, input().split())))
  
  max_profit = -1
  def recur(d, profit):
    nonlocal max_profit
    if d >= n + 1:
      if max_profit < profit:
        max_profit = profit
      return

    if (d + profits[d][0] <= n + 1):
      recur(d + profits[d][0], profit + profits[d][1])
    recur(d + 1, profit)

  recur(1, 0)
  return max_profit

if __name__ == '__main__':
  print(solution())