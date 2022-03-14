'''
  풀이
    주어진 폴리오미노의 길이가 각각 4, 2로, 길이 4인 폴리오미노가 길이가 2인 폴리오미노 2개를 대체할 수 있다.
    또한, 길이가 4인 폴리오미노가 AAAA로, 길이가 2인 폴리오미노 BB보다 사전순으로 앞선다.
    따라서, 주어진 보드판에서 XXXX를 먼저 폴리오미노 AAAA로 치환한 후 남은 XX에 대해 폴리오미노 BB로 치환하면 된다.
    만약 치환 후 보드판에 X가 남아있다면 불가능한 것이므로 -1을 출력하면 된다.
'''

def solution():
  board = input().replace('XXXX', 'AAAA').replace('XX', 'BB')
  print(board if not board.count('X') else -1)
  
if __name__ == '__main__':
  solution()