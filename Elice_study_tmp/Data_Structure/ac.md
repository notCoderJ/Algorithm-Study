# 💢AC

## 🔸 풀이 과정

- ### 풀이 아이디어

  해당 문제는 함수 'R(뒤집기)'과 'D(첫 번째 원소 삭제)'로 이루어진 명령들과 배열이 주어지면 주어진 배열에서 해당 연산들을 수행한 후 결과를 출력하는 문제이다. 따라서 주어진 배열의 원소들을 deque에 넣고 수행할 함수들을 하나씩 수행한 후 그 결과를 출력하면 해결할 수 있다.
  여기서, deque을 이용한 것은 deque이 앞과 뒤에서 모두 O(1)의 시간복잡도로 삭제가 가능한 자료구조이기 때문이다. 이는 'D' 함수를 수행할 때의 로직과 관련이 있다.

* 수행 알고리즘
  - 각 함수 수행 로직
    1. 'R' 함수  
       해당 배열을 뒤집는 함수지만, 실제로 배열을 역순으로 정렬하게 되면 O(NlogN)의 시간복잡도가 계속 누적되어 효율성이 나빠진다. 따라서, 'direction'이라는 현재 배열의 앞을 가리키는 변수를 하나 두어 'R'함수가 수행될 때마다 이 값만 변경하도록 하였다.
    2. 'D' 함수
       먼저, 현재 배열의 남아있는 원소를 확인한 후 원소가 없다면 더 이상 삭제 연산이 불가능하므로 "error"를 출력하고 이후 과정을 생략한다. 반대의 경우 현재 direction이 가리키는 위치에서 배열의 원소를 제거한다.
  - 결과 출력
    "error"가 출력되는 경우는 이전 'D' 함수를 수행하는 로직에서 처리해주었고 반대로 배열의 원소가 존재하는 경우는 변수 direction 값에 따라 해당 배열을 앞이나 뒤에서 부터 출력하도록 하였다.

<br>

- [구현한 소스 코드](ac.py)

        import sys
        from collections import deque
        input = sys.stdin.readline

        t = int(input())

        for _ in range(t):
            p = input()
            n = int(input())
            nums = input()
            if n == 0:  # 주어진 배열이 없는 경우
                if 'D' in p:
                    print("error")
                else:
                    print('[]')
                continue
            nums = deque(list(nums.strip()[1:-1].split(',')))
            direction = 0

            for cmd in p:
                if cmd == 'R':
                    # 0과 -1 중 하나의 값을 선택하여 배열의 끝단에서 원소를 제거한다.
                    direction = -1 if direction == 0 else 0
                elif cmd == 'D':
                    if len(nums) == 0:
                        print("error")
                        break
                    nums.popleft() if direction == 0 else nums.pop()
            else:
                print(f'[{",".join(list(nums))}]' if direction == 0 else f'[{",".join(list(nums)[::-1])}]')
