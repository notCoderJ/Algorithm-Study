def solution(numbers, target):
    if not numbers:
        if target == 0:
            return 1
        else:
            return 0

    return solution(numbers[1:], target - numbers[0]) + solution(numbers[1:], target + numbers[0])