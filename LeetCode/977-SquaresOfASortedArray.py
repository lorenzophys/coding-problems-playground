"""
LINK: https://leetcode.com/problems/squares-of-a-sorted-array/

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
 
Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?
"""


 
def sortedSquares_simple(nums):
    for i in range(len(nums)):
        nums[i]= nums[i] * nums[i]

    return sorted(nums)


def sortedSquares_efficent(nums):
    left = 0
    right = len(nums) - 1
    spots = len(nums) - 1
    result = [None] * len(nums)
    
    for count in range(spots, -1, -1):
        if abs(nums[left]) > abs(nums[right]):
            result[count] = nums[left] * nums[left]
            left += 1
        else:
            result[count] = nums[right] * nums[right]
            right -= 1
        
    return result