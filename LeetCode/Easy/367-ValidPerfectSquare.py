"""
LINK: https://leetcode.com/problems/valid-perfect-square/

Given a positive integer num, write a function which returns True if num is a perfect square else False.
Follow up: Do not use any built-in library function such as sqrt.

Example 1:

Input: num = 16
Output: true

Example 2:

Input: num = 14
Output: false
 
Constraints:

1 <= num <= 2^31 - 1
"""


def isPerfectSquare(num):
    if num==1:
        return True
    
    right = num//2
    left = 1
    
    while left<=right:
        mid = (right+left)//2
        
        if mid*mid==num:
            return True
        elif mid*mid<num:
            left = mid + 1
        else:
            right = mid - 1
            
    return False