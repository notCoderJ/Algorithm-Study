# 계수 정렬 알고리즘
import random

def counting_sort(target):
    # 정렬할 리스트의 모든 데이터에 대해 카운팅하기 위한 리스트를 0으로 초기화하여 생성한다
    count_list = [0] * (max(target) + 1)
    # 정렬할 리스트의 모든 데이터를 카운팅한다
    for i in target:
        count_list[i] += 1
    
    # 정렬한 데이터 값인 인덱스 값을 카운팅 수 만큼 순차적으로 출력한다
    for val, cnt in enumerate(count_list):
        print((str(val) + ' ') * cnt, end='')


target = [random.randrange(0, 101) for _ in range(100)]
counting_sort(target)