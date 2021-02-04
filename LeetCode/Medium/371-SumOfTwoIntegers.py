"""
LINK: https://leetcode.com/problems/sum-of-two-integers/

Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example 1:

Input: a = 1, b = 2
Output: 3

Example 2:

Input: a = -2, b = 3
Output: 1
Accepted
"""


# Incomplete solution
def getSum(a, b):
    """
    a XOR b is the sum
    a AND b is the carry
    If there is a nonzero carry, add the carry to the sum and shift the carry to the left. Repeat until the carry is zero.
    """
    sum = a ^ b
    carry = a & b
    
    while carry:
        sum ^= carry
        carry <<= 1
        
    return sum