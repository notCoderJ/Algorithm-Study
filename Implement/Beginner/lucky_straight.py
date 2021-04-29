# 현재 캐릭터 점수를 자릿수 기준으로 반으로 나누어 왼쪽 부분의 각 자릿수 합과
# 오른쪽 부분의 각 자릿수 합이 동일할 때 '럭키 스트레이트'를 발동할 수 있다.
# 현재 점수 N이 주어질 때 '럭키 스트레이트'를 사용할 수 있는 지 확인해라.


n = input()

half_idx = len(n) // 2
left = sum(map(int, n[:half_idx]))
right = sum(map(int, n[half_idx:]))

if left == right:
    print("LUCKY")
else:
    print("READY")


''' TEST
123402
''' # LUCKY
'''
7755
''' # READY