def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    high = 0
    low = len(people) - 1

    while high < low:
        if people[high] + people[low] <= limit:
            answer += 1
            low -= 1
        high += 1

    # 총 인원에서 2명씩 탑승한 보트 수를 빼주면 전체 사용한 보트 수가 된다
    answer = len(people) - answer
    return answer