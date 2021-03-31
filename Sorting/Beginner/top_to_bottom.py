# 주어진 수열을 내림차순으로 정렬해라.

n = int(input())
num_list = [int(input()) for _ in range(n)]

# counting sort
print("counting sort : ", end=' ')
count_list = [0] * (max(num_list) + 1)

for i in num_list:
    count_list[i] += 1

for i in range(len(count_list)-1, -1, -1):
    for j in range(count_list[i]):
        print(i, end=' ')

print()

# version 1
print("version 1 : ", end=' ')
for i in sorted(num_list, reverse=True):
    print(i, end=' ')

print()

# version 2
num_list.sort(reverse=True)

print("version 2 : ", end=' ')
for i in num_list:
    print(i, end=' ')