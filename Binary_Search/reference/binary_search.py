# 이진 탐색
import random

# version 1 - 재귀 함수
def recur_binary_search(target, start, end, data_list):
    if start > end: # 찾을 대상이 리스트에 없으면 None을 리턴한다.
        return None

    mid = (start + end) // 2 
    if target == data_list[mid]: # 대상을 찾았으면 대상의 위치를 리턴한다
        return mid + 1
    # 대상이 중간 값보다 큰 경우 중간 값의 우측에 대해 이진 탐색을 수행한다.
    elif target > data_list[mid]: 
        return recur_binary_search(target, mid + 1, end, data_list)
    # 대상이 중간 값보다 작은 경우 중간 값의 좌측에 대해 이진 탐색을 수행한다.
    else:
        return recur_binary_search(target, start, mid - 1, data_list)
    

# version 2 - 반복문
def binary_search(target, data_list):
    start = 0
    end = len(data_list) - 1

    while start <= end:
        mid = (start + end) // 2
        if target == data_list[mid]: # 대상을 찾았으면 대상의 위치를 리턴한다
            return mid + 1
        # 대상이 중간 값보다 큰 경우 시작 인덱스를 중간 인덱스 바로 다음으로 변경한다
        elif target > data_list[mid]:
            start = mid + 1
        # 대상이 중간 값보다 작은 경우 끝 인덱스를 중간 인덱스 바로 전으로 변경한다
        else:
            end = mid - 1
    return None


data_list = [random.randrange(1, 101) for _ in range(10)]
data_list.sort()
target = data_list[random.randrange(0, 10)]
print(target, data_list, sep=', ')
print(recur_binary_search(target, 0, len(data_list) - 1, data_list))
# print(binary_search(target, data_list))