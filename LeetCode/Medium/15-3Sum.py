"""
LINK: https://leetcode.com/problems/3sum/

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:

Input: nums = []
Output: []

Example 3:

Input: nums = [0]
Output: []
 
Constraints:

0 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""


def threeSum(nums):
    result = []
    nums.sort()
    
    for index, value in enumerate(nums):
        target = -1 * value
        left = index + 1
        right = len(nums) - 1
        
        while left<right:
            sum = nums[left] + nums[right]
            
            if sum>target:
                right -= 1
            elif sum<target:
                left += 1
            else:
                three = [value, nums[left], nums[right]]
                if three not in result:
                    result.append(three)
                left += 1
                right -= 1

    return result


def threeSum_faster(nums):
    """
    This skips the duplicates directly
    """
    result = []
    nums.sort()
    
    for index, value in enumerate(nums):
        if not index or (index and nums[index]!=nums[index-1]):
            target = -1 * value
            left = index + 1
            right = len(nums) - 1

            while left<right:
                sum = nums[left] + nums[right]

                if sum>target:
                    right -= 1
                elif sum<target:
                    left += 1
                else:
                    result.append([value, nums[left], nums[right]])
                    
                    while left<right and nums[left]==nums[left+1]:
                        left += 1
                    while left<right and nums[right]==nums[right-1]:
                        right -= 1
                        
                    left += 1
                    right -= 1

    return result