'''
  새로 알게된 점
    print(*수열)과 print(' '.join(문자열 원소로 된 수열)) 이 둘에 속도 차이가 있었다!
    
    일단, 먼저 간단히 뇌피셜로 생각해보면(뇌피셜이기 때문에 당연히 틀릴 수 있다!)
      print(*수열)은 각 원소에 대해 내부적으로 출력을 여러번 수행하는 것이고,
      print(' '.join(수열))은 수열의 각 원소를 돌며 하나의 문자열로 변환하고
      이를 내부에서 출력할 때 한번에 연속적으로 출력하는 것이기 때문에 차이가 있는 것이 아닐까 생각한다.
      결론은 출력을 여러 번 하냐 안하냐로 인해 속도 차이가 있는 것이 아닐까하는 생각이 든다...
      
      하지만, 한편으론 만약 주어지는 수열의 크기가 커진다면 유의미한 속도 차이가 있을 것인가라는 생각도 든다.
      결국 join을 하기 위해서는 합칠 수열의 크기만큼 반복을 수행해야 할텐데 수열의 크기가 커진다면 이를 수행 후 출력하는 시간이나
      그냥 원소 하나씩 출력하는 시간이나 크게 차이가 있을까 싶기도 하다...
      실제로 아래 주석과 같이 테스트를 수행해봤을 때
      수열의 크기가 100만정도 되면 그냥 출력 시 약 17초 정도 변환 후 출력 시 약 16초 정도가 측정되었다.
      수열의 크기가 작아지면 약 2배 정도의 시간 차가 나왔는데 애초에 수행 시간 자체가 적어서 크게 의미있을지는 모르겠다.
      
    이에 대한 정확한 내용은 print의 동작 매커니즘을 알아보고 이해해야 확실히 알 수 있을 것 같다.
    추후 이에 대해 한번쯤 학습해볼 필요가 있다고 생각한다.
'''

import sys
input = lambda: sys.stdin.readline().strip()

def solution(cnt, seq):
  if cnt == m:
    print(' '.join(seq))
    return
  
  for i in nums:
    seq[cnt] = str(i)
    solution(cnt + 1, seq)

if __name__ == '__main__':
  n, m = map(int, input().split())
  nums = list(sorted(map(int, input().split())))
  solution(0, [0] * m)


# TEST CODE
# import time

# start1 = time.time()
# print(*range(10_000))
# end1 = time.time()

# nums = map(str, range(10_000))
# start2 = time.time()
# print(' '.join(nums))
# end2 = time.time()
# print(f'seq: {end1 - start1}')
# print(f'str: {end2 - start2}')