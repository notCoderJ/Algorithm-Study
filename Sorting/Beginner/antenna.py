# 일직선상의 마을에 위치한 집 중 한 곳에 안테나를 설치할 때
# 안테나로부터 모든 집까지의 거리의 총합이 최소가 되도록하는 안테나의 위치는?
# (한 곳에 여러 집이 위치할 수 있고 안테나 설치 위치가 여러 곳일 경우 가장 낮은 값을 출력)

n = int(input())
locations = list(map(int, input().split()))
locations.sort()

# my code
# 안테나가 설치되는 지점으로부터 모든 집과의 거리의 합을 구한다.
dist = lambda x: -sum(locations[:x]) + sum(locations[x:]) + (2 * x - n) * locations[x]
distance = [ (dist(i), locations[i]) for i in range(len(locations))]

print(min(distance)[1])

# answer code
'''
    간단히 생각하면
    주어진 집들 간의 거리가 정해져있는 상황에서
    중간 지점이 아닌 어느 한쪽에 치우쳐 안테나를 설치하면
    안테나의 설치 지점을 기준으로 집의 수가 한쪽은 많아지고 반대쪽은 적어지므로
    양측 간 집의 수의 차이 * |중간 지점의 집 위치 - 현재 안테나가 설치된 위치|만큼 거리가 증가한다.
    따라서, 주어진 집들 중 중간 지점에 위치한 집에 안테나를 설치해야 거리의 총합이 최소가 된다.
'''
print(locations[(n - 1) // 2])


''' TEST
4
5 1 7 9
''' # 5