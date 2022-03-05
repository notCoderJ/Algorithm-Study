'''
  풀이
    이전에 프로그래머스에서 풀었던 큰 수 만들기랑 비슷한 문제인 줄 알았는데... 같은 문제였다 ㅎㅎ?
    
    풀이 방법은 간단하다.
    주어진 수를 한 자리씩 순회하며 현재 숫자와 스택에 있는 수들을 비교한다.
    스택에 있는 수가 현재 숫자보다 작다면 스택에 있는 수를 하나씩 제거하고 제거 카운트를 1씩 감소시킨다.
    스택이 비어있거나 스택에 있는 수들이 현재 숫자보다 크거나 제거 카운트가 0이면 스택에 현재 숫자를 추가한다.
    
    주어진 수를 모두 순회하고나면 현재 스택에 남은 숫자들을 조합하여 출력하면 된다.
    여기서, 주의할 점은 순회가 끝난 후에도 제거 카운트가 0이 아닌 경우 스택의 뒤부터 제거 카운트만큼 제거하고 조합해야 한다.
      예를 들어 주어진 숫자가 7654처럼 내림차순으로 주어진다면
      k가 2라고 가정해도 순회가 끝난 후 스택에는 7, 6, 5, 4가 그대로 남아있기 때문이다!
'''

import sys
input = lambda: sys.stdin.readline().strip()

def solution(n, k, number):
  cnt = k
  st = []
  for i in number:
    if not st:
      st.append(i)
      continue
    
    while cnt and st and st[-1] < i:
      st.pop()
      cnt -= 1
    st.append(i)
    
  print(''.join(st[:len(st) - cnt]))

if __name__ == "__main__":
  n, k = map(int, input().split())
  number = input()
  solution(n, k, number)