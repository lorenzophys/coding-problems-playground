"""
LINK: https://leetcode.com/problems/pascals-triangle-ii/

Given an integer rowIndex, return the rowIndexth row of the Pascal's triangle.
Notice that the row index starts from 0.
In Pascal's triangle, each number is the sum of the two numbers directly above it.

Follow up:
Could you optimize your algorithm to use only O(k) extra space?

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]

Example 2:

Input: rowIndex = 0
Output: [1]

Example 3:

Input: rowIndex = 1
Output: [1,1]
 
Constraints:

0 <= rowIndex <= 33
"""


def getRow(rowIndex):
    if not rowIndex:
        return [1]
    elif rowIndex==1:
        return [1,1]
    
    layer = [1,1]
    for row in range(rowIndex-1):
        new = [1]
        for index, current in enumerate(layer[1:], 1):
            previous = layer[index-1]
            new.append(current+previous)
            
        new.append(1)
        layer = new

    return layer