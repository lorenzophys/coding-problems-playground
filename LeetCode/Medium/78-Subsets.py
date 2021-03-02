"""
LINK: https://leetcode.com/problems/subsets/

Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:

Input: nums = [0]
Output: [[],[0]]
 
Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
"""


def subsets(nums):
    result = []
    current = []
    
    search(0, nums, current, result)
    
    return result


def search(index, nums, current, result):
    result.append(current)
    for i in range(index, len(nums)):
        search(i+1, nums, current+[nums[i]], result)