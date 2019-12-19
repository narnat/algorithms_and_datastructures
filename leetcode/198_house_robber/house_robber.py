#!/usr/bin/python3
""" House Robber Problem"""

class Solution:
    def rob(self, nums):
        max_prev = 0
        curr_max = 0
        for i in nums:
            new_max = max(i + max_prev, curr_max)
            max_prev = curr_max
            curr_max = new_max
        return curr_max


a = Solution().rob([1, 2, 3, 1])
assert a == 4

print(a)
