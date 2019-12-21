#!/usr/bin/python3

""" Counting inversions """

def merge(l, r, m, arr, sub_arr):
    i, j = l, m
    inv_n = 0
    for k in range(l, r + 1):
        if (i < m) and (j > r or arr[i] <= arr[j]):
            sub_arr[k] = arr[i]
            i += 1
        else:
            inv_n += m - i + 1
            j += 1
    return inv_n

def merge_sort(l, r, arr, sub_arr):

    inv_n = 0
    if l < r:
        m = (r + l) // 2
        merge_sort(l, m, arr, sub_arr)
        merge_sort(m + 1, r, arr, sub_arr)
        merge(l, r, m, arr, sub_arr)
    return inv_n

def merge_1(arr, l, m, r): 
    n1 = m - l + 1
    n2 = r- m
    inv_n = 0 
  
    left = [0] * (n1) 
    right = [0] * (n2) 
  
    for i in range(0 , n1): 
        left[i] = arr[l + i] 
  
    for j in range(0 , n2): 
        right[j] = arr[m + 1 + j] 
  
    i = 0     # Initial index of first subarray 
    j = 0     # Initial index of second subarray 
    k = l     # Initial index of merged subarray 
  
    while i < n1 and j < n2 : 
        if left[i] <= right[j]: 
            arr[k] = left[i] 
            i += 1
        else:
            inv_n += m - i + 1
            arr[k] = right[j] 
            j += 1
        k += 1
  
    while i < n1: 
        arr[k] = left[i] 
        i += 1
        k += 1
  
    while j < n2: 
        arr[k] = right[j] 
        j += 1
        k += 1
    
    return inv_n

def countInversions(arr):
    sub_arr = arr.copy()
    res = merge_sort(0, len(arr) - 1, arr, sub_arr)
    return res 


# ans1 = countInversions([1, 1, 1, 2, 2])
ans2 = countInversions([2, 1, 3, 1, 2])

# assert ans1 == 0 and ans2 == 4

# print(ans1)
print(ans2)
