import unittest as ut


def union_sets(gate, next_gate):
    docking = find(gate, next_gate)  # 현재 들어온 비행기가 도킹할 탑승구
    if docking == 0:  # 도킹할 탑승구가 존재하지 않으면 도킹 실패를 반환한다
        return False
    next_gate[docking] = find(docking - 1, next_gate)
    return True


def find(gate, next_gate):
    if gate != next_gate[gate]:
        next_gate[gate] = find(next_gate[gate], next_gate)
    return next_gate[gate]


def solution(gates, next_gate):
    max_cnt = 0
    for gate in gates:
        if not union_sets(gate, next_gate):
            break
        max_cnt += 1
    return max_cnt


g = int(input())
p = int(input())

gates = [int(input()) for _ in range(p)]
next_gate = [i for i in range(g + 1)]

print(solution(gates, next_gate))


''' TEST
4
3
4
1
1

4
6
2
2
3
3
4
4
'''  # 2 3


class TestGate(ut.TestCase):
    def test_gate_4_plane_3(self):
        gates = [4, 1, 1]
        next_gate = [0, 1, 2, 3, 4]
        self.assertEqual(solution(gates, next_gate), 2)

    def test_gate_4_plane_6(self):
        gates = [2, 2, 3, 3, 4, 4]
        next_gate = [0, 1, 2, 3, 4]
        self.assertEqual(solution(gates, next_gate), 3)


ut.main()
