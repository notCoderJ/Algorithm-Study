'''
  풀이
    주어진 배열당 최대 갯수가 4,000개까지이므로 완전 탐색의 경우 O(N^4)으로 시간초과가 분명했다.
    그래서, 먼저 배열을 두 개씩 쪼개서 각각 모든 합을 구한 새로운 배열 2개를 만들고,
    서로 반대 부호의 값이 상대 배열에 존재하는지 확인하며 카운트하는 방식으로 풀었다.
    그럼에도 무한의 시간초과 굴레에 빠져 엄청난 고통을 받았다...
    
    처음에는 원인 파악이 안되서 최대한 for문 수나 데이터 연산 로직을 최소화시키는데 집중했다.
    하지만, 시간초과의 고통에서 벗어날 수 없었고...;;
    일단, 풀이 내역을 보니 파이썬으로는 통과한 사람이 1년간 딱 한명 있었는데 이마저도 테스트 케이스의 차이인지 확실치 않았다.
    그래서 pypy로 제출해야했고 그럼에도 시간초과에서 벗어나지는 못했다.
    
    구글링을 하다가 시간초과 원인을 알고 나니 너무 어이가 없었다.
    처음에는 defaultdict를 사용해서 풀었는데, 이것이 원인이었다.
    일반 dict로 수정하고 get메소드를 사용하니 통과되었다..........
    허허... 혹시 이부분이 원인일까봐 구글링했을 때는
    defaultdict와 dict의 get메소드 성능 비교를 해놓은 글에서 defaultdict가 약 2배정도 빠르다고 했는데...쩝
'''

import sys
input = lambda: sys.stdin.readline().strip()

def solution():
  n = int(input())
  arr = [list(map(int, input().split())) for _ in range(n)]
  
  sum_ab = {}
  for i in range(n):
    for j in range(n):
      sum_ab[arr[i][0] + arr[j][1]] = sum_ab.get(arr[i][0] + arr[j][1], 0) + 1
  
  answer = 0
  for i in range(n):
    for j in range(n):
      answer += sum_ab.get(-(arr[i][2] + arr[j][3]), 0)
        
  print(answer)
  
if __name__ == '__main__':
  solution()