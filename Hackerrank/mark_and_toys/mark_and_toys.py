#!/usr/bin/python3

"""Comments are coming soon"""

def maximumToys(prices, k):
    prices.sort()
    s = 0
    for i in range(len(prices)):
        s += prices[i]
        if s > k:
            return i
    return i
