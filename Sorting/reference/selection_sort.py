# 선택 정렬 알고리즘

def selection_sort(target):
    length = len(target)
    for i in range(0, length - 1):
        min_idx = i # 정렬되지 않은 맨 앞의 인덱스를 최소값의 인덱스라 가정한다
        for j in range(i + 1, length):
            if target[min_idx] > target[j]: # 현재 최소값보다 작은 값이 있으면 최소값 인덱스를 변경한다
                min_idx = j
        # 찾은 최소값과 정렬되지 않은 맨 앞의 값을 서로 교환한다
        target[i], target[min_idx] = target[min_idx], target[i]
        
    return target


target = [22, 50, 17, 25, 18, 32, 33, 44, 29, 8]
print(selection_sort(target))