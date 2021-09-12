import sys
input = lambda: sys.stdin.readline().strip()

def solution(cnt, seq):
  if cnt == m:
    print(' '.join(seq[1:]))
    return
  
  for i in nums:
    if int(seq[-1]) > i:
      continue
    
    seq.append(str(i))
    solution(cnt + 1, seq)
    seq.pop()

if __name__ == '__main__':
  n, m = map(int, input().split())
  nums = list(sorted(map(int, input().split())))
  solution(0, [0])