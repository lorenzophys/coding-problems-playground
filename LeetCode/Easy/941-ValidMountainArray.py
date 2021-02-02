"""
LINK https://leetcode.com/problems/valid-mountain-array/

Given an array of integers arr, return true if and only if it is a valid mountain array.
Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Example 1:

Input: arr = [2,1]
Output: false

Example 2:

Input: arr = [3,5,5]
Output: false

Example 3:

Input: arr = [0,3,2,1]
Output: true
 
Constraints:

1 <= arr.length <= 104
0 <= arr[i] <= 104
"""


def validMountainArray(arr):
    left = 0
    right = len(arr) - 1
    
    if len(arr)<3:
        return False
    
    for i in range(right):
        if arr[left]<arr[left+1]:
            left += 1
        else:
            break
            
    for i in range(right, left-1, -1):
        if arr[right]<arr[right-1]:
            right -= 1
        else:
            break
    
    if left == right and left!=0 and right!=len(arr)-1:
        return True
        
    return False