"""
LINK: https://leetcode.com/problems/power-of-three/

Given an integer n, return true if it is a power of three. Otherwise, return false.
An integer n is a power of three, if there exists an integer x such that n == 3x.

Example 1:

Input: n = 27
Output: true

Example 2:

Input: n = 0
Output: false

Example 3:

Input: n = 9
Output: true

Example 4:

Input: n = 45
Output: false
 
Constraints:

-231 <= n <= 231 - 1

Follow up: Could you do it without using any loop / recursion?
"""


def isPowerOfThree(n):
    if not n:
        return False
    
    while not n%3:
        n /= 3
        
    return n==1


def isPowerOfThree_recursive(n):
    if not n:
        return False
    elif n==1:
        return True
    elif not n%3:
        return isPowerOfThree_recursive(n/3)
    
    return False