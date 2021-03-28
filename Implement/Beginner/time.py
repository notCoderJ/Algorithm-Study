# 시간 00:00:00 ~ N:59:59까지 3이 포함된 모든 경우의 수는?

# 문제 유형:
#   입력한 시간 범위 내에 주어진 조건을 만족하는 모든 경우의 수를 찾아야하므로 '완전 탐색' 유형에 속한다

n = int(input())

count = 0
# 모든 시간을 검사한다 가정해도 24 * 60 * 60 = 86,400 경우의 수만 나오므로
# 값을 하나씩 증가시키며 문자열로 바꿔 '3'이 포함되는지 검사하면 된다
for h in range(n + 1):
    for m in range(60):
        for s in range(60):
            time = str(h) + str(m) + str(s)
            if '3' in time:
                count += 1

print (count)