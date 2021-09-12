import sys
input = lambda: sys.stdin.readline().strip()

def solution(cnt, seq):
  if cnt == m:
    print(*seq[1:])
    return
    
  for i in range(1, n + 1):
    if seq[-1] > i:
      continue
    
    seq.append(i)
    solution(cnt + 1, seq)
    seq.pop()

if __name__ == '__main__':
  n, m = map(int, input().split())
  solution(0, [0])