#!/usr/bin/python3

""" Fraudulent activity """
MAX_AMOUNT_EXPENDITURE = 201

def get_median(count_arr, median_idx):
    count = -1
    res = 0
    for i in range(MAX_AMOUNT_EXPENDITURE):
        if count_arr[i] > 0:
            count += count_arr[i]
        if count >= median_idx[0]:
            res = i
            if len(median_idx) > 1:
                if count < median_idx[1]:
                    for j in (i + 1, MAX_AMOUNT_EXPENDITURE):
                        if count_arr[j] > 0:
                            res = (res + j) / 2
                            break
            break

    return res

def activityNotifications(expenditure, d):
    count_arr = [0] * MAX_AMOUNT_EXPENDITURE
    l = len(expenditure)
    notifications = 0
    median_idx = (d // 2,) if d % 2 else (d // 2 - 1, d // 2)

    for i in range(d):
        count_arr[expenditure[i]] += 1

    for i in range(d,l):
        median = get_median(count_arr, median_idx)
        if expenditure[i] >= 2 * median:
            notifications += 1
        count_arr[expenditure[i]] += 1
        count_arr[expenditure[i - d]] -= 1

    return notifications

ans1 = activityNotifications([2, 3, 4, 2, 3, 6, 8, 4, 5], 5)
ans2 = activityNotifications([1, 2, 3, 4, 4], 4)
ans3 = activityNotifications([10, 20, 30, 40, 50], 3)

assert ans1 == 2 and ans2 == 0 and ans3 == 1

print(ans1)
print(ans2)
print(ans3)
