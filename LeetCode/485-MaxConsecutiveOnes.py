"""
LINK: https://leetcode.com/problems/max-consecutive-ones/

Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:

Input: [1,1,0,1,1,1]
Output: 3

Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.

Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
"""


def findMaxConsecutiveOnes(nums):

    counter = 0
    max_ones = 0
    
    for num in nums:
        if num:
            counter += 1
            if counter > max_ones:
                max_ones = counter
        else:
            counter = 0
    return max_ones