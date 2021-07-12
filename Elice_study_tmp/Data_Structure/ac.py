import sys
from collections import deque
input = sys.stdin.readline


t = int(input())

for _ in range(t):
    p = input()
    n = int(input())
    nums = input()
    if n == 0:
        if 'D' in p:
            print("error")
        else:
            print('[]')
        continue
    nums = deque(
        list(nums.strip()[1:-1].split(',')))
    direction = 0  # direction - front(0), back(-1)

    for cmd in p:
        if cmd == 'R':
            direction = -1 if direction == 0 else 0
        elif cmd == 'D':
            if len(nums) == 0:
                print("error")
                break
            nums.popleft() if direction == 0 else nums.pop()
    else:
        print(f'[{",".join(list(nums))}]' if direction ==
              0 else f'[{",".join(list(nums)[::-1])}]')


'''
4
RDD
4
[1,2,3,4]
DD
1
[42]
RRD
6
[1,1,2,3,5,8]
D
0
[]
'''
