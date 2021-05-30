from itertools import product

def solution(numbers, target):
    pair = [(-x, x) for x in numbers]
    values = list(map(sum, product(*pair)))
    
    return values.count(target)