from collections import defaultdict

def solution(tickets):
    answer = []
    
    have_tickets = defaultdict(list)

    # 출발 공항별로 티켓을 분리
    for start, dest in tickets:
        have_tickets[start].append(dest)
    
    # 출발 공항별로 도착 공항들을 알파벳 역순으로 정렬
    for start in have_tickets.keys():
        have_tickets[start].sort(reverse=True)
    
    visited = ["ICN"]
    while visited:
        start = visited[-1]
        if have_tickets[start]:
            visited.append(have_tickets[start].pop())
        else: # 더 이상 도착 가능한 공항이 없으면 경유했던 경로에 추가
            answer.append(visited.pop())

    return answer[::-1] # 최종 도착 공항부터 기록했으므로 역순으로 반환