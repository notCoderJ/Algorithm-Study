# 한 마을에 N개의 집과 M개의 도로가 있고 모든 도로에는 가로등이 있다. 이 가로등을 하루 동안
# 켜기위한 비용은 도로의 길이와 같다. 임의의 두 집에 대해 가로등이 켜진 도로만 오갈 수
# 있도록 하면서 일부 가로등을 비활성화하여 최대 절약할 수 있는 금액은?
# (각 집은 0 ~ N-1번까지로 구분된다.)


import unittest as ut


def union_sets(house1, house2, connected):
    conn_house1 = find_root(house1, connected)
    conn_house2 = find_root(house2, connected)

    # cycle 발생, 이동 가능한 다른 경로가 존재하므로 해당 도로를 제외한다
    if conn_house1 == conn_house2:
        return False
    elif conn_house1 > conn_house2:
        connected[conn_house1] = conn_house2
    else:
        connected[conn_house2] = conn_house1
    return True


def find_root(house, connected):
    if house != connected[house]:
        connected[house] = find_root(connected[house], connected)
    return connected[house]


def solution(roads, connected):
    save_cost = 0
    for h1, h2, cost in roads:
        # 절약할 수 있는 최대 비용을 구하는 것이므로 제외된 도로들의 비용을 합한다
        if not union_sets(h1, h2, connected):
            save_cost += cost
    return save_cost


# n, m = map(int, input().split())
# roads = [tuple(map(int, input().split())) for _ in range(m)]
# roads.sort(key=lambda x: x[2])
# connected = [i for i in range(n)]

# print(solution(roads, connected))


''' TEST
7 11
0 1 7
0 3 5
1 2 8
1 3 9
1 4 7
2 4 5 
3 4 15
3 5 6
4 5 8
4 6 9
5 6 11
'''  # 51


class TestDarkRoad(ut.TestCase):
    def test_solution(self):
        n, m = 7, 11
        roads = [(0, 1, 7),
                 (0, 3, 5),
                 (1, 2, 8),
                 (1, 3, 9),
                 (1, 4, 7),
                 (2, 4, 5),
                 (3, 4, 15),
                 (3, 5, 6),
                 (4, 5, 8),
                 (4, 6, 9),
                 (5, 6, 11)]
        roads.sort(key=lambda x: x[2])
        connected = [i for i in range(n)]

        self.assertEqual(solution(roads, connected), 51)


ut.main()
