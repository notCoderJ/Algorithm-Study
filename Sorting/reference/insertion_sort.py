# 삽입 정렬 알고리즘

def insertion_sort(target):
    for i in range(1, len(target)):
        for j in range(i, 0, -1):
            # 현재 값과 바로 이전 값을 비교하고 이전 값이 더 클 경우 값을 서로 교환한다
            if target[j] < target[j-1]:
                target[j-1], target[j] = target[j], target[j-1]
            else: # 더 이상 앞으로 이동할 수 없으면 멈춘다
                break

    return target


target = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2]
print(insertion_sort(target))