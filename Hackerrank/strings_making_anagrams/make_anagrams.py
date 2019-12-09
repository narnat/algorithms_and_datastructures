#!/usr/bin/python3

def makeAnagram(a, b):
    d_a = {}
    for c in a:
        if c not in d_a:
            d_a[c] = 1
        else:
            d_a[c] += 1

    for c in b:
        if c not in d_a:
            d_a[c] = 1
        else:
            d_a[c] -= 1
    c = 0
    a = list(d_a.values())
    return sum(a)

if __name__ == '__main__':
    input = [("cde", "abc"),
             ("fcrxzwscanmligyxyvym", "jxwtrhvujlmrpdoqbisbwhmgpmeoke"),
             ("showman", "woman")]

    for i in input:
        res = makeAnagram(i[0], i[1])
        print(res)
