# 수열의 원소 중 그 값이 인덱스와 동일한 원소를 고정점이라고 할 때
# N개의 '서로 다른 원소를 포함'하고 오름차순으로 정렬된 수열에서 고정점을 출력하시오.
# (없으면 -1을 출력하고 O(logN) 알고리즘으로 설계해야 한다.)


def binary_search(start, end, sequence):
    if start > end:
        return -1

    middle = (start + end) // 2
    if middle == sequence[middle]:
        return middle
    # 중간 인덱스 < 중간 위치 값인 경우 우측은 무조건 위치 값이 인덱스보다 크므로 좌측에 대해 검사한다
    elif middle < sequence[middle]:
        return binary_search(start, middle - 1, sequence)
    # 중간 인덱스 > 중간 위치 값인 경우 좌측은 무조건 위치 값이 인덱스보다 작으므로 우측에 대해 검사한다
    else:
        return binary_search(middle + 1, end, sequence)

n = int(input())
sequence = list(map(int, input().split()))
print(binary_search(0, len(sequence) - 1, sequence))


''' TEST
5
-15 -6 1 3 7

7
-15 -4 2 8 9 13 15

7
-15 -4 3 8 9 13 15
''' # 3 2 -1