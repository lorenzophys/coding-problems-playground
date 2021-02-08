"""
LINK: https://leetcode.com/problems/3sum-closest/

Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
 
Constraints:

3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4
"""


def threeSumClosest(nums, target):
    nums.sort()
    gap = float('inf')
    
    for index, value in enumerate(nums):
        left, right = index + 1, len(nums) - 1
        
        while left<right:
            sum = value + nums[left] + nums[right]
            
            dist = abs(target - sum)
            if dist<abs(gap):
                gap = target - sum
            
            if sum<target:
                left += 1
            elif sum>target:
                right -= 1
            else:
                return target
            
    return target - gap