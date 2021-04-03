# 고유 정수 번호가 적혀있는 N개의 부품 중에 손님이 주문한 M개의 종류가 모두 있는지 확인해라
# 있으면 yes, 없으면 no를 공백으로 구분해 출력
# 조건 :
#   1. 1 <= N <= 1,000,000 / 1 <= 고유 번호 <= 1,000,000
#   2. 1 <= M <= 100,000 / 1 <= 요구 번호 <= 1,000,000,000

import sys

# version 1 - 이진 탐색
def binary_search(target, start, end, parts):
    if start > end: # 찾는 부품이 없으면 Flase를 리턴한다
        return False
    
    mid = (start + end) // 2
    if target == parts[mid]: # 대상 부품을 찾았으면 True를 리턴한다
        return True
    # 대상 부품 번호가 중간 번호보다 크면 중간 번호 우측에 대해 이진 탐색을 수행한다
    elif target > parts[mid]:
        return binary_search(target, mid + 1, end, parts)
    # 대상 부품 번호가 중간 번호보다 작으면 중간 번호 좌측에 대해 이진 탐색을 수행한다
    else:
        return binary_search(target, start, mid - 1, parts)


n = int(input())
part_numbers = list(map(int, input().split()))

m = int(input())
target_list = list(map(int, sys.stdin.readline().rstrip().split()))

# version 1
part_numbers.sort()

for tg in target_list:
    if binary_search(tg, 0, n-1, part_numbers):
        print("yes", end=' ')
    else:
        print("no", end=' ')

# version 2 - 계수 정렬
# count_list = [0] * (max(part_numbers) + 1) # 최대값을 구하는 O(n)의 연산이 추가됨
# 가능한 고유 번호 범위 전체를 생성 => 추가 연산은 없지만 메모리가 더 소모됨
# count_list = [0] * 1000000
# for num in part_numbers:
#     count_list[num] = 1

# for tg in target_list:
#     # 요구 부품이 있는지 확인한다(단, 문제는 조건2의 10억 범위라는 것인데... 이 경우 인덱스 초과로 에러가 발생한다)
#     if count_list[tg] == 1:
#         print("yes", end=' ')
#     else:
#         print("no", end=' ')

# version 3 - 집합(set)을 이용
# set 자료형은 key값만 존재하며 중복 요소를 허용하지 않는다
# in 연산 시 해시 테이블 접근으로 하나씩 순회하는 리스트 자료형에 비해 속도가 매우 빠르다
# for tg in target_list:
#     if tg in set(part_numbers):
#         print("yes", end=' ')
#     else:
#         print("no", end=' ')

''' TEST CASE
5
8 3 7 9 2
3
5 7 9
''' # no yes yes