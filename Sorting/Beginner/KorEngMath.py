# N명의 학생 이름과 국어, 영어, 수학 점수가 주어질 때 다음 조건으로 학생의 성적을 정렬하시오.
# 정렬 조건 :
#   1. 국어 점수가 감소하는 순서로
#   2. 국어 점수가 같으면 영어 점수가 증가하는 순서로
#   3. 국어, 영어 점수가 같으면 수학 점수가 감소하는 순서로
#   4. 모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로

n = int(input())
students = []

for _ in range(n):
    name, kor, eng, math = input().split()
    students.append((name, int(kor), int(eng), int(math)))

# 국어(내림차) -> 영어(오름차) -> 수학(내림차) -> 이름(오름차)
students.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

print()

for student in students:
    print(student[0])


''' TEST
12
Junkyu 50 60 100
Sangkeun 80 60 50
Sunyoung 80 70 100
Soong 50 60 90
Haebin 50 60 100
Kangsoo 60 80 100
Donghyuk 80 60 100
Sei 70 70 70
Wonseob 70 70 90
Sanghyun 70 70 80
nsj 80 80 80
Taewhan 50 60 90
'''
# Answer
'''
Donghyuk
Sangkeun
Sunyoung
nsj
Wonseob
Sanghyun
Sei
Kangsoo
Haebin
Junkyu
Soong
Taewhan
'''