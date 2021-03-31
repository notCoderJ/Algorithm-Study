# 퀵 정렬 알고리즘

# 일반적인 퀵 정렬 알고리즘
def quick_sort(start, end, target):
    # 리스트의 시작 인덱스가 마지막 인덱스보다 크거나 같으면
    # 분할된 리스트에 데이터가 없거나 1개이므로 정렬을 종료한다
    if start >= end:
        return

    pivot = start # 시작 인덱스를 피벗 인덱스로 설정한다
    left = pivot + 1 # 좌측 시작 인덱스를 설정한다
    right = end # 우측 시작 인덱스를 설정한다

    # 좌측 인덱스가 우측 인덱스보다 작거나 같을 동안만 다음 교환 로직을 수행한다
    while left <= right:
        # 좌측 시작 값부터 피벗보다 큰 값을 찾을 때까지 인덱스를 하나씩 증가시킨다
        while left <= end and target[left] <= target[pivot]:
            left += 1
        # 우측 시작 값부터 피벗보다 작은 값을 찾을 때까지 인덱스를 하나씩 감소시킨다
        # 우측 인덱스가 시작 인덱스보다 작아지지 않도록 주의!!(피벗 교환을 위해)
        while right > start and target[right] >= target[pivot]:
            right -= 1
        if left >= right:# 좌우측 인덱스 값이 동일하거나 엇갈린 경우 피벗과 좌우측 값 중 작은 값의 위치를 서로 교환한다
            target[pivot], target[right] = target[right], target[pivot]
        else: # 아닌 경우 좌우측 값의 위치를 서로 교환한다
            target[left], target[right] = target[right], target[left]

    # 분할된 리스트에 대해 퀵 정렬을 반복 수행한다.
    quick_sort(start, right-1, target)
    quick_sort(right+1, end, target)

    return target

# *** 파이썬의 장점을 살린 퀵 정렬 알고리즘 ***
def python_quick_sort(target):
    list_len = len(target)
    if list_len <= 1: # 분할된 리스트에 데이터가 없거나 1개면 해당 리스트를 리턴한다
        return target 
    
    pivot = target[0] # 0번 인덱스의 값을 피벗으로 설정한다
    remain_list = target[1:] # 피벗을 제외한 리스트를 구한다

    # 피벗 값과 같거나 작은 값을 모아 좌측 리스트로 분할한다
    left_list = [i for i in remain_list if pivot >= i]
    # 피벗 값보다 큰 값을 모아 우측 리스트로 분할한다
    right_list = [i for i in remain_list if pivot < i]

    # 좌우측 분할된 리스트와 피벗을 합쳐 피벗을 기준으로 정렬된 리스트를 리턴한다
    return python_quick_sort(left_list) + [pivot] + python_quick_sort(right_list)


target = [3, 44, 38, 5, 47, 15, 36, 26, 27]
# print(quick_sort(0, len(target)-1, target))
print(python_quick_sort(target))
