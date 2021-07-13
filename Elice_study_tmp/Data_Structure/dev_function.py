'''
    문제 요약:
        각 기능은 진도가 100%일 때 서비스에 반영되고 뒤에 있는 기능이 먼저 개발될 수 있습니다.
        이 경우 앞에 있는 기능이 배포될 때 뒤에 있는 기능도 함께 배포됩니다.
        먼저 배포해야 하는 순서대로 각 작업의 진도 progresses와 각 작업의 개발 속도 speeds가 주어질 때
        각 배포마다 몇 개의 기능이 배포되는지를 return 하도록 solution 함수를 완성하세요.

    풀이 요약:
        각 기능의 완료일을 구하면서 이전 기능 완료일과 현재 기능 완료일을 비교하여
        현재 기능 완료일이 클 경우에만 이전 기능들의 수를 answer에 추가하고
        이전 기능 완료일 값을 현재 기능 완료일 값으로 갱신하는 과정을 수행한다.
        위 과정이 모두 끝나면 마지막에 카운트되지 않은 기능들의 수를 answer에 추가해준다.
'''


def solution(progresses, speeds):
    answer = []

    prev = 0
    pre_day = 0
    for work, progress in enumerate(progresses):
        ''' 기존 작성한 코드
        days, r = divmod(100 - progress, speeds[work])
        days = days if r == 0 else days + 1
        '''
        # 변경 코드: 음수의 몫 계산 시 -1 되는 것이 절댓값으론 1만큼 커진다...
        days = -((progress - 100) // speeds[work])

        if work == 0:
            pre_day = days
        elif pre_day < days:
            # 이전 작업일 수보다 현재 작업일 수가 많을 경우 이전 작업들의 수를 추가한다
            answer.append(work - prev)
            pre_day = days
            prev = work

    # 마지막에 카운트되지 않은 작업들의 수를 추가해준다.
    answer.append(len(progresses) - prev)

    return answer
