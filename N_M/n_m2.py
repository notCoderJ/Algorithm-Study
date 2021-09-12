import sys
input = lambda: sys.stdin.readline().strip()

def solution(start, cnt, seq):
  if cnt == m:
    print(*seq)
    return
    
  for i in range(start + 1, n + 1):
    seq[cnt] = i
    solution(seq[cnt], cnt + 1, seq)

if __name__ == "__main__":
  n, m = map(int, input().split())
  solution(0, 0, [0] * m)