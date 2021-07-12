import sys
import heapq
input = sys.stdin.readline


n = int(input())
pq = []

for _ in range(n):
    nums = list(map(int, input().split()))
    for num in nums:
        heapq.heappush(pq, num)
    while len(pq) > n:
        heapq.heappop(pq)

print(heapq.heappop(pq))


'''
5
12 7 9 15 5
13 8 11 19 6
21 10 26 31 16
48 14 28 35 25
52 20 32 41 49
'''
