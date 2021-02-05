"""
LINK: https://leetcode.com/problems/intersection-of-two-arrays/

Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]

Note:

Each element in the result must be unique.
The result can be in any order.
"""


def intersection(nums1, nums2):
    hashset1 = set(nums1)
    hashset2 = set(nums2)
    result = []
    
    for value in hashset1:
        if value in hashset2:
            result.append(value)
            
    return result