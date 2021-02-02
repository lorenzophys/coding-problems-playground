"""
LINK: https://leetcode.com/problems/rotate-array/

Given an array, rotate the array to the right by k steps, where k is non-negative.

Follow up:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?
 
Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
 
Constraints:

1 <= nums.length <= 2 * 104
-231 <= nums[i] <= 231 - 1
0 <= k <= 105
"""


def rotate(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """
    result = [None] * len(nums)
    for index, value in enumerate(nums):
        rotated_index = (index + k) % len(nums)
        result[rotated_index] = value
        
    nums[:] = result


def rotate_multipleReverse(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """
    def reverse(start, end):
        while start<end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    k %= len(nums)
    n = len(nums) - 1
    start, end = 0, n
    
    # Reverse all
    reverse(0, n)
        
    # Reverse first part
    reverse(0, k-1)
        
    # Reverse second part
    reverse(k, n)