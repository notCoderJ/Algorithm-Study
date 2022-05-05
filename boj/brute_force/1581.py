'''
  풀이
    주어진 조건에 맞춰 각각의 경우를 다음과 같이 나누어서 풀었다.
      1) fs == 0 and ff != 0
        -> 빠른 시작이 있는 경우 빠른 시작 첫 스타트이므로 ff만 포함할 수 있다.
      2) fs == 0 and ff == 0
        -> sf로 시작한 순간 f로 시작하는 곡이 필요하므로 ss를 먼저 다 포함하고 sf를 마지막에 1개 포함한다.
      3) fs != 0
        -> 먼저, ff와 ss를 모두 포함시키고 마지막에 sf와 fs 서로 반복해서 포함시킨다.
          예를 들어, 다음과 같은 순서로 포함시키면 된다.
            ff -> ... -> ff -> fs -> ss -> ... -> ss -> sf -> fs -> sf -> ...
          그럼, ff + ss + min(fs, sf) * 2가 되는데
          여기서, fs > sf라면 마지막에 fs가 한번 더 올 수 있기 때문에 이를 고려해줘야 한다.
          (추가로, ff == 0 or ss == 0은 상관없다 -> 단순히 위에서 해당 부분만 빼면 되므로)
'''

import sys
input = lambda: sys.stdin.readline().strip()

def solution(ff, fs, sf, ss):
  if fs == 0:
    return ff if ff != 0 else ss + [0, 1][sf != 0]
  else:
    return ff + ss + min(fs, sf) * 2 + [0, 1][fs > sf]

if __name__ == '__main__':
  ff, fs, sf, ss = map(int, input().split())
  print(solution(ff, fs, sf, ss))