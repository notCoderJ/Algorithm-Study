# 오름차순으로 정렬된 N개의 원소를 가진 수열 중 x의 횟수는?

# x의 등장 횟수를 세는 함수
def count_by_value(x, sequence):
    total_len = len(sequence)
    first = first_index(x, 0, total_len - 1, sequence)
    cnt = -1
    if first: # x값이 존재할 경우
        last = last_index(x, first, total_len - 1, sequence)
        cnt = last - first + 1

    return cnt

# 첫 번째 등장하는 x의 인덱스를 찾는 함수
def first_index(target, start, end, sequence):
    if start > end:
        return None

    mid = (start + end) // 2

    # 중간 값이 x이면서 중간 인덱스가 0에 도달했거나 중간 인덱스 - 1의 값이 x보다 작으면 현재 중간 인덱스를 반환
    if (mid == 0 or sequence[mid - 1] < target) and sequence[mid] == target:
        return mid
    elif sequence[mid] >= target:
        return first_index(target, start, mid - 1, sequence)
    else:
        return first_index(target, mid + 1, end, sequence)

# 마지막으로 등장하는 x의 인덱스를 찾는 함수
def last_index(target, start, end, sequence):
    if start > end:
        return None

    mid = (start + end) // 2

    # 중간 값이 x이면서 중간 인덱스가 끝에 도달했거나 중간 인덱스 + 1의 값이 x보다 크면 현재 중간 인덱스를 반환
    if (mid == len(sequence) - 1 or sequence[mid + 1] > target) and sequence[mid] == target:
        return mid
    elif sequence[mid] > target:
        return last_index(target, start, mid - 1, sequence)
    else:
        return last_index(target, mid + 1, end, sequence)


# 2. python module bisect
from bisect import bisect_left, bisect_right

def simple_count_by_value(x, sequence):
    left = bisect_left(sequence, x)
    right = bisect_right(sequence, x)
    cnt = right - left

    return cnt if cnt else -1


n, x = map(int, input().split())

sequence = list(map(int, input().split()))

# print(count_by_value(x, sequence))
print(simple_count_by_value(x, sequence))


''' TEST
7 2
1 1 2 2 2 2 3
''' # 4
''' TEST2
7 4
1 1 2 2 2 2 3
''' # -1