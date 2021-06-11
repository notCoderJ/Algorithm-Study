def dfs(depart, tickets):
    route = []
    for i in range(len(tickets)):
        if tickets[i][0] == depart:
            route = dfs(tickets[i][1], tickets[:i] + tickets[i+1:])
            if len(route) == len(tickets):
                break

    return [depart] + route

def solution(tickets):
    answer = []
    tickets.sort(key=lambda x: (x[0], x[1]))
    answer = dfs("ICN", tickets)
    
    return answer