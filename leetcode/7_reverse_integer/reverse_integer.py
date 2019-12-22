#!/usr/bin/python3
""" Reverse Integer"""

def reverse(x: int) -> int:
        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2 ** 31
        
        rev = 0
        sign = -1 if x < 0 else 1
        x = abs(x)
        while x:
            rev = rev * 10 + x % 10
            x //= 10 

        rev = rev * sign
        return 0 if rev > INT_MAX or rev < INT_MIN else rev

print(reverse(231))