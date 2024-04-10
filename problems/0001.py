from baseClass import Problem
import time

def solve():
    # Brute force solution
    result = 0
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            result += i
    return result


task = Problem(1)
task.solve(solve)