import sys
input = lambda: sys.stdin.readline().rstrip()

def sequence(cnt, seq, visited):
  if cnt == m:
    print(*seq)
    return
  
  for i in range(1, n + 1):
    if visited[i]:
      continue
    
    visited[i] = True
    seq[cnt] = i
    sequence(cnt + 1, seq, visited)
    visited[i] = False
    
if __name__ == "__main__":
  n, m  = map(int, input().split())
  visited = [False] * (n + 1)
  sequence(0, [0] * m, visited) #