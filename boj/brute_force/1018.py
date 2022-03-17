'''
  풀이
    먼저, 주어진 보드의 최대 크기가 50 * 50이고, 만들려는 체스판의 크기가 8 * 8이므로
    보드를 43 * 43번 반복하며, 체스판의 크기만큼씩(8 * 8) 다시 칠할 개수를 확인하면 된다.
    43 * 43 * 64 = 118,336번의 연산으로 해결할 수 있으므로 완전 탐색으로 풀 수 있다.
    
    주어진 보드를 행과 열 각각 43번씩 순회하며,
    각 체스판에 대해 min(화이트로 시작한 판의 다시 칠할 개수, 블랙으로 시작한 판의 다시 칠할 개수)를 구하고
    현재 최소값과 비교해 작은 값을 선택하는 것을 반복한다.
'''

def solution():
  n, m = map(int, input().split())
  board = [input() for _ in range(n)]
  
  cnt = 64
  for i in range(n - 7):
    for j in range(m - 7):
      paint = [0, 0] # w, b
      for r in range(8):
        for c in range(8):
          if board[i + r][j + c] == 'W':
            paint[not ((r + c) & 1)] += 1
          else:
            paint[(r + c) & 1] += 1
      else:
        cnt = min(cnt, min(paint))
  return cnt

if __name__ == '__main__':
  print(solution())