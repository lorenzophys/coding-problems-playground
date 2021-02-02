"""
LINK: https://leetcode.com/problems/rotate-array/


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