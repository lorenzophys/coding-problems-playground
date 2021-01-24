"""
LINK: https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 
Constraints:

2 <= nums.length <= 103
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

"""


def twoSum_simple(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            sum_ = nums[i] + nums[j]
            if sum_==target:
                return [i, j]
            elif sum_>target:
                continue


def twoSum_efficient(nums, target):
    hashmap = {}
    for index, value in enumerate(nums):
        complement = target - value
        if complement in hashmap:
            return [hashmap[complement], index]
        else:
            hashmap[value] = index