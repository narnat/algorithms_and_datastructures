#!/usr/bin/python3
import math
""" Minimum time required problem """

def minTime(machines, goal):
    l_bound = math.ceil(min(machines) * goal / len(machines)) 
    r_bound = math.ceil(max(machines) * goal / len(machines))

    while l_bound < r_bound:
        mid = (l_bound + r_bound) // 2
        s = sum(mid // i for i in machines)
        if s < goal:
            l_bound = mid + 1
        else:
            r_bound = mid
    
    return r_bound




ans1 = minTime([2, 3], 5)
ans2 = minTime([1, 3, 4], 10)
ans3 = minTime([2, 3, 2], 10)
ans4 = minTime([4, 5, 6], 12)



print(ans1)
print(ans2)
print(ans3)
print(ans4)

assert ans1 == 6 and ans2 == 7 and ans3 == 8 and ans4 == 20