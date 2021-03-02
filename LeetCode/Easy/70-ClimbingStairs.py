"""
LINK: https://leetcode.com/problems/climbing-stairs/

You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 
Constraints:

1 <= n <= 45
"""


def climbStairs_bruteForce(n):
    if n<0:
        return 0
    elif n==0:
        return 1
    else:
        return self.climbStairs(n-1) + self.climbStairs(n-2) 


def climbStairs(n):
    return self.climb(n, {})


def climb(left, memo):
    if left<0:
        return 0
    elif left==0:
        return 1
    elif left in memo.keys():
        return memo[left]
        
    memo[left] = climb(left-1, memo) + climb(left-2, memo)
    
    return memo[left]
    