'''
  풀이
    주어진 n의 범위가 1 ~ 100,000이므로 완전 탐색으로 부분합을 구하려면 O(N^2) ~= 약 100,000^2으로 불가능.
    
    이 문제의 경우 2가지 방법으로 접근이 가능했다.
    1. 투포인터 사용
      "연속된 수들의 부분합"을 구하는 것이므로 먼저, n개의 수를 순회하며 각 지점에서의 총합을 구해놓는다.
      (i ~ j까지의 부분합은 sum(1 ~ j) - sum(1 ~ i - 1)과 같다.)
      이후 좌측과 우측 두 지점의 인덱스를 동일하게 0부터 시작하여 두 지점의 총합 차를 S와 비교하며 다음 과정을 반복하면 된다.
        총합 차 >= S이면 길이를 더 줄여도 되므로 좌측 지점의 인덱스를 증가시키고 현재 길이와 저장된 길이 중 최소값을 기록한다.
        총합 차 < S 이면 길이를 더 늘려 값을 키워야하므로 우측 지점의 인덱스를 증가시킨다.
    
    2. 이분탐색 사용
      구하고자 하는 것은 부분합이 S 이상를 만족하는 최소 길이이므로
      부분합 길이를 이분 탐색 대상으로 잡고 Parametric Search를 적용하면 된다.
      이 경우 이분 탐색 시 매 중간값에 대해 큐를 사용하여 해당 길이만큼의 부분합을 모두 계산하면서 S 이상을 만족하는지 확인해도 되지만
      이렇게 하면 시간 복잡도를 O(NlogN)에서 줄일 수 없다.
      조금 더 시간 복잡도를 줄이기 위해 투포인터에서 사용했던 방법을 적용하여 각 지점에서의 총합을 구해놓고,
      이분 탐색 시 중간 값에 대해 해당 길이 인덱스부터
      좌측(인덱스 0부터 증가), 우측(현재 인덱스의 값) 두 지점의 총합 차를 계산하고 S와 비교하며 최소 길이를 구하면 된다.
'''

import sys
input = lambda: sys.stdin.readline().strip()

# 1. 투포인터
def solution():
  _, s = map(int, input().split())
  nums = list(map(int, input().split()))
  
  sums = [0]
  for i in nums:
    sums.append(sums[-1] + i)
  
  answer = 100001
  left, right = 0, 0
  while right < len(sums):
    partial = sums[right] - sums[left]
    if partial < s:
      right += 1
    else:
      answer = min(answer, right - left)
      left += 1
    
  print(answer if answer != 100001 else 0)
  
# 2. 이분탐색
def solution2():
  answer = 0
  n, s = map(int, input().split())
  nums = list(map(int, input().split()))
  sums = [0]
  for i in nums:
    sums.append(sums[-1] + i)
  
  def partial(target):
    for i, p in enumerate(sums[target:]):
      if p - sums[i] >= s:
        return True
    return False
  
  left, right = 1, n
  while left <= right:
    mid = (left + right) // 2
    if partial(mid):
      right = mid - 1
      answer = mid
    else:
      left = mid + 1

  print(answer)
  
if __name__ == "__main__":
  solution()
  solution2()