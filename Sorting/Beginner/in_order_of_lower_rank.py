# N명의 학생에 대한 이름과 성적이 주어질 때 성적이 낮은 순으로 이름을 출력해라.

n = int(input())

# version 1 - 딕셔너리
students = {}
for _ in range(n):
    student = input().split()
    students[student[0]] = int(student[1])

# 딕셔너리의 sorted는 기본적으로 value를 기준으로 정렬한 후 key값을 리스트로 리턴한다
for name in sorted(students):
    print(name, end=' ')


# version 2 - 튜플
students = []
for _ in range(n):
    student = input().split()
    students.append((student[0], int(student[1])))

# 람다식을 이용해 성적을 key값으로 하여 정렬한다
for name, rank in sorted(students, key=lambda student : student[1]):
    print(name, end=' ')