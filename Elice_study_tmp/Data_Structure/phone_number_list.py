'''
    문제 요약:
        전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지
        확인하여 있으면 false 없으면 true를 출력한다.
        예)
            구조대 : 119
            박준영 : 97 674 223
            지영석 : 11 9552 4421
            구조대의 번호는 지영석의 번호의 접두어이므로 false를 출력
            
    풀이 요약:
        공통 - 주어진 전화번호부를 ascii코드상 오름차 순으로 정렬하고 각 번호를 순회하면서
            
        1번 풀이 - 연속한 두 번호 중 짧은 번호의 길이를 구하여 해당 길이만큼 두 번호를 비교하고
                  같으면 false를 반환, 전화번호부 순회가 끝날 때까지 없는 경우 true를 반환한다.
                  
        2번 풀이 - 해당 번호에 대해 앞에서부터 한글자씩 늘려가며 그 값이 접두어를 검사하는
                   chkPrefix 딕셔너리에 있는 지 확인한다.
                   만약 있는 경우 false를 반환하고 없는 경우 현재 번호를 chkPrefix 딕셔너리에 추가한다. 
                   for문이 종료될 때까지 false 값을 반환하지 않으면 가능한 접두어가 없는 것이므로
                   true를 반환한다.
'''


def solution(phone_book):
    answer = True
    phone_book.sort()

    for i in range(len(phone_book) - 1):
        min_len = min(len(phone_book[i]), len(phone_book[i + 1]))
        if phone_book[i + 1].startswith(phone_book[i][:min_len]):
            return False

    # chkPrefix = {}
    # for num in phone_book:
    #     for i in range(1, len(num) + 1):
    #         if chkPrefix.get(num[:i]):
    #             return False
    #     chkPrefix[num] = True

    return answer
