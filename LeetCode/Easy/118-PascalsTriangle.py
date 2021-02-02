"""
LINK: https://leetcode.com/problems/pascals-triangle/

Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""


def generate(numRows):
    # Edge cases, if numRows<0 LeetCode expects a non-empty triangle
    if not numRows:
        return []
    elif numRows<0 or numRows==1:
        return[[1]]
    
    triangle = [
        [1],
        [1,1],
    ]
    
    for row in range(1, numRows-1):
        new = [1]
        layer = triangle[row]
        for index, current in enumerate(layer[1:], 1):
            previous = layer[index-1]
            new.append(current+previous)
        new.append(1)
        triangle.append(new)
        
    return triangle