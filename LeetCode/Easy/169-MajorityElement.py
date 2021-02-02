"""
LINK: https://leetcode.com/problems/majority-element/

Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3

Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-231 <= nums[i] <= 231 - 1
 
Follow-up: Could you solve the problem in linear time and in O(1) space?
"""

# O(n) space
def majorityElement_simple(nums):
        lookup = {}
        for value in nums:
            if value in lookup:
                lookup[value] += 1
            else:
                lookup[value] = 1
                
        length = len(nums)
        for key, value in lookup.items():
            if value>length/2:
                return key


# Boyer-Moore: https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm
def majorityElement_efficent(nums):
    majority = 0
    count = 0
    
    for value in nums:
        if count==0:
            majority = value
            
        if value==majority:
            count += 1
        else:
            count -= 1
            
    return majority