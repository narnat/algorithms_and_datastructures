#!/usr/bin/python3
"""Max sub array problem"""

def maximumSum(a, m):
    prefix = [[None, i + 1] for i in range(len(a))]  # Create prefix array

    curr = 0
    maxi = float('-inf') 
    for i in range(len(a)):                          # Fill prefix array
        curr = (a[i] % m + curr) % m
        prefix[i][0] = curr
        if maxi < curr:
            if m - curr < 2:
                return curr                          # If m - 1 is found (the highest possible number), return
            maxi = curr
    prefix.sort()                                    # Sort prefix array: similar to     
                                                     # prefix.sort(key = lambda x : x[0])

    mini = float('inf')
    for i in range(len(a) - 1):
        if prefix[i][1] > prefix[i + 1][1]:
            if prefix[i + 1][0] - prefix[i][0] < mini:
                mini = prefix[i + 1][0] - prefix[i][0]
    return max(maxi, m - mini)

ans1 = maximumSum([3, 3, 9, 9, 5], 7)
ans2 = maximumSum([1, 2, 3], 2)
ans3 = maximumSum([1, 5, 9], 5)

print(ans1)
print(ans2)
print(ans3)

assert ans1 == 6 and ans2 == 1 and ans3 == 4
