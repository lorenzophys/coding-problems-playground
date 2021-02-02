"""
LINK: https://leetcode.com/problems/factorial-trailing-zeroes/

Given an integer n, return the number of trailing zeroes in n!.
Follow up: Could you write a solution that works in logarithmic time complexity?


Example 1:

Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.

Example 2:

Input: n = 5
Output: 1
Explanation: 5! = 120, one trailing zero.

Example 3:

Input: n = 0
Output: 0
 

Constraints:

0 <= n <= 104
"""


def trailingZeroes(n):
    fives = 0
    while n:
        fives += n//5
        n //= 5
            
    return fives


def trailingZeroes_recursive(n):
    if not n:
        return 0
    else:
        return n//5 + trailingZeroes_recursive(n//5)