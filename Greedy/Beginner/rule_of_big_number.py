# 다양한 수로 이루어진 배열의 수들을 M번 더할 때 최댓값?
# (단, 하나의 수를 K번 연속 더할 수 없고 같은 수일지라도 인덱스가 다르면 다른 수로 판단)
# ex. 2, 4, 5, 6, 7 / M = 5 / K = 2 => 7 + 7 + 6 + 7 + 7

# 문재 파악 포인트:
#   1. 더하기 위해 선택 가능한 수가 둘 이상이다
#   2. 각 상황에서 문제의 조건을 고려해 가능한 '가장 큰 수를 선택'해야 한다
#   3. 결과 값이 '최댓값'이다
#   따라서, 그리디 알고리즘을 적용해 해결할 수 있다

n, m, k = map(int, input().split())
num_list = list(map(int, input().split()))

first_max = max(num_list)
num_list.remove(first_max)
second_max = max(num_list)

# 반복되는 특성을 파악하자!
# 문제 해결을 위해 가장 큰 수가 K번, 그 다음 큰 수가 1번 나열되는 구조가 반복된다!
# 예를 들어 first_max = 4, second_max = 3, k=2일 때 (4 + 4 + 3) + (4 + 4 + 3) + ...

quotient, remainder = divmod(m, k+1)
result = (quotient * k + remainder) * first_max # 반복 횟수 * 연속된 k값 + 남은 횟수 == 가장 큰 수의 배치 개수
result += quotient * second_max # 반복 횟수 == 그 다음 큰 수의 배치 개수

print(result)