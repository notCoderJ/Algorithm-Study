'''
    문제 요약
        주어진 수식에서 올바른 괄호 쌍을 제거하여 가능한 수식들을 모두 출력한다.
        예) 수식 (2+(2*2)+2)가 주어지면
            가능 : (2+2*2+2), 2+(2*2)+2, 2+2*2+2
            불가능 :  (2+2*2)+2, 2+(2*2+2) (올바른 괄호 쌍이 제거되지 않았으므로)

    풀이 요약
        해당 문제는 재귀를 이용해 풀 수 있는 문제 같았다. 하지만 조합을 이용해서도
        풀 수 있을 것 같다고 생각하여 조합으로 시도를 해보았다.
        
        1. 주어진 수식을 순회하며 여는 괄호의 인덱스를 모두 스택에 넣고 닫는 괄호가
            나오면 스택에서 하나씩 꺼내 dict[꺼낸 값] = 닫는 괄호의 인덱스 로 딕셔너리를 생성한다.

        2. 조합을 이용해 1번에서 생성한 딕셔너리의 key에 대한 멱집합을 구한다.
        
        3. 2번에서 구한 멱집합의 각 원소들에 대해 key값과 쌍을 이루는 value(닫는 괄호 인덱스)들을 합하여
            각 경우마다 제거할 괄호의 인덱스 리스트를 구한다.
        
        4. 3번에서 구한 리스트를 순회하며 각 경우에서 괄호가 제거된 수식을 구하고 결과에 추가해준다.
        
        5. 사전순으로 출력해야 하므로 결과를 정렬시키고 출력한다.
'''

from itertools import combinations

result = set()
math_exp = input()

pr_idx = {}
st = []
for i, c in enumerate(math_exp):
    if c == '(':
        st.append(i)
    elif c == ')':
        pr_idx[st.pop()] = i

for n in range(1, len(pr_idx) + 1):
    for case in combinations(pr_idx, n):
        exp = ''
        pre = 0
        for cur in sorted(list(case) + [pr_idx[x] for x in case]):
            exp += math_exp[pre:cur]
            pre = cur + 1

        exp += math_exp[pre:]
        result.add(exp)

print(*sorted(result), sep="\n")
