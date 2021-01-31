"""
LINK: https://leetcode.com/problems/count-primes/

Count the number of prime numbers less than a non-negative number, n.

Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

Example 2:

Input: n = 0
Output: 0

Example 3:

Input: n = 1
Output: 0
 
Constraints:

0 <= n <= 5 * 106
"""


def countPrimes_simple(n):
    primes = [True for _ in range(n)]
    solution = 0
    i = 2
    
    while i*i<n:
        if primes[i]:
            j = 2
            while i*j<n:
                primes[i*j] = False
                j += 1
        i += 1
            
    for index, value in enumerate(primes):
        if value and index not in (0, 1):
            solution += 1
            
    return solution


def countPrimes_fast(n):
    primes = [True for _ in range(n)]
    solution = 0
    
    for i in range(2,int(n**0.5)+1):
        if primes[i]:
            for j in range(i*i, n, i):
                primes[j] = False
            
    for index, value in enumerate(primes):
        if value and index not in (0, 1):
            solution += 1
            
    return solution


def countPrimes_faster(n):
    primes = [1 for _ in range(n)]
    solution = 0
    
    if n>2:
        primes[0], primes[1] = 0, 0
    else:
        return 0
    
    for i in range(2,int(n**0.5)+1):
        if primes[i]:
            for j in range(i*i, n, i):
                primes[j] = 0
            
    return sum(primes)