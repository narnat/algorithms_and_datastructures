#!/usr/bin/python3

"""Comments are coming soon"""
def climbingLeaderboard(scores, alice):
    scores_l = len(scores)
    rank = [0] * scores_l

    for i in range(scores_l):
        if i == 0:
            rank[i] = 1
        else:
            rank[i] = rank[i - 1]
            if scores[i - 1] != scores[i]:
                rank[i] += 1

    j = scores_l - 1

    result = []
    for i in range(len(alice)):
        ans = 1
        while j > 0 and alice[i] > scores[j]:
            j -= 1
        if alice[i] == scores[j]:
            ans = rank[j]
        elif alice[i] < scores[j]:
            ans = rank[j] + 1

        result.append(ans)

    return result




if __name__ == '__main__':
    scores = [[100, 100, 50, 40, 40, 20, 10], [100, 90, 90, 80, 75, 60]]
    alice = [[5, 25, 50, 120], [50, 65, 77, 90, 102]]
    assertion = [[6, 4, 2, 1], [6, 5, 4, 2, 1]]

    check = True
    printing = True

    for i in zip(scores, alice, assertion):
        scores_i = i[0]
        alice_i = i[1]
        assertion_i = i[2]
        res = climbingLeaderboard(scores_i, alice_i)
        if check:
            try:
                assert res == assertion_i
                print("You passed this test case!!!")
            except AssertionError:
                print("********************")
                print(f"Wrong answer\n Your output\n {res}\n Expected\n {assertion_i}")
                print("********************")
