"""
LINK: https://leetcode.com/problems/search-insert-position/

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4

Example 4:

Input: nums = [1,3,5,6], target = 0
Output: 0

Example 5:

Input: nums = [1], target = 0
Output: 0
 
Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
"""


def searchInsert_simple(nums, target):
    if target<nums[0]:
        return 0
    elif target>nums[-1]:
        return len(nums)
    
    for index, value in enumerate(nums):
        if value>=target:
            return index


def searchInsert_binarySearch(nums, target):
    if target<nums[0]:
        return 0
    elif target>nums[-1]:
        return len(nums)
    
    left, right = 0, len(nums) - 1
    
    while left<right:
        mid = (left+right)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            left += 1
        else:
            right -= 1
            
    return right