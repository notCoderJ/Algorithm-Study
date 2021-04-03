# N개의 길이가 일정하지 않은 떡들을 절단기로 한번에 잘라서
# 잘린 부분을 손님이 요청한 M만큼 주려고 할 때 설정 가능한 절단기 높이 최대값?

# version 1 - 재귀적 풀이
def recur_binary_search(target, start, end, rice_cakes):
    if start > end: # 절단기를 조절할 범위가 남지 않았으면 종료
        return None

    mid = (start + end) // 2

    # 떡들을 절단기로 자르고 남은 부분들의 총 길이를 구한다
    parts_sum = sum([rc - mid for rc in rice_cakes if rc > mid])
    if target > parts_sum: # 요구한 길이보다 적게 남은 경우 절단기 높이를 줄인다(좌측에 대해 이진 탐색)
        return binary_search(target, start, mid - 1, rice_cakes)
    else: # 요구한 길이보다 많이 남은 경우 절단기 높이를 높인다(우측에 대해 이진 탐색)
        # 요구한 길이와 같거나 많이 남아야 하므로 절단기 높이를 기록한다
        result = binary_search(target, mid + 1, end, rice_cakes)
        return result if result else mid

# version 2 - 반복문 풀이
def binary_search(target, start, end, rice_cakes):
    while start <= end: # 절단기를 조절할 수 있을 때까지 이진 탐색
        parts_sum = 0
        mid = (start + end) // 2
        
        for rc in rice_cakes:
            if rc > mid: # 떡들을 절단기로 자르고 남은 부분들의 총 길이를 구한다
                parts_sum += rc - mid
        
        # 요구한 길이보다 적게 남은 경우 절단기 높이를 줄인다(좌측에 대해 이진 탐색)
        if target > parts_sum:
            end = mid -1
        else: # 요구한 길이보다 많이 남은 경우 절단기 높이를 높인다(우측에 대해 이진 탐색)
            result = mid # 요구한 길이와 같거나 많이 남아야 하므로 절단기 높이를 기록한다
            start = mid + 1

    return result


n, m = map(int, input().split())
rice_cakes = list(map(int, input().split()))

print(recur_binary_search(m, 0, max(rice_cakes), rice_cakes))
# print(binary_search(m, 0, max(rice_cakes), rice_cakes))

''' TEST CASE
4 6
19 15 10 17
''' # 15