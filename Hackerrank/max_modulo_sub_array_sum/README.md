# Maximum Subarray

# Sum

We define the following:

A subarray of array of length is a contiguous segment from through where
.
The sum of an array is the sum of its elements.
Given an -element array of integers, , and an integer, , determine the maximum value of the sum of
any of its subarrays modulo. For example, Assume and. The following table lists all
subarrays and their modulus:

(^) [ 1 sum] 1 1 % 2
[[ 23 ]] (^23  )
[[ 12 ,, 23 ]] (^35  )
[ 1 , 2 , 3 ] 6 0
The maximum modulus is.
**Function Description**
Complete the maximumSum function in the editor below. It should return a long integer representing the
maximum value of.
maximumSum has the following parameter(s):
a: an array of long integers, the array to analyze
m: a long integer, the modulo divisor
**Input Format**
The first line contains an integer , the number of queries to perform.
The next pairs of lines are as follows:
The first line contains two space-separated integers divisor. and (long) , the length of and the modulo
The second line contains space-separated long integers.
**Constraints**
the sum of over all test cases
**Output Format**
For each query, return the maximum value of as a long integer.
**Sample Input**


(^1) 5 7
3 3 9 9 5
**Sample Output**
6
**Explanation**
The subarrays of array and their respective sums modulo are ranked in order of
length and sum in the following list:
1. and
and
2.

## 3.

## 4.

## 5.

The maximum value for for any subarray is.