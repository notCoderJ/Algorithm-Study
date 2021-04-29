# 공포도가 X인 모험가는 X명 이상으로 구성된 모험가 그룹에 참가해야 한다.
# N명의 모험가 정보가 주어졌을 때 여행을 떠날 수 있는 그룹 수의 최대값?

n = int(input())

adventurers = list(map(int, input().split()))
adventurers.sort() # 공포도가 낮은 모험가부터 그룹을 생성해야 최대 그룹 수가 나온다

members = 0 # 그룹에 속한 모험가 수
group = 0 # 결성된 그룹 수

for fear in adventurers:
    members += 1
    if members >= fear:
        group += 1
        members = 0

print(group)


''' TEST
5
2 3 1 2 2
''' # 2