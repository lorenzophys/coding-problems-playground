"""
LINK: https://leetcode.com/problems/find-lucky-integer-in-an-array/

Given an array of integers arr, a lucky integer is an integer which has a frequency in the array equal to its value.
Return a lucky integer in the array. If there are multiple lucky integers return the largest of them. If there is no lucky integer return -1.

Example 1:

Input: arr = [2,2,3,4]
Output: 2
Explanation: The only lucky number in the array is 2 because frequency[2] == 2.

Example 2:

Input: arr = [1,2,2,3,3,3]
Output: 3
Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.

Example 3:

Input: arr = [2,2,2,3,3]
Output: -1
Explanation: There are no lucky numbers in the array.

Example 4:

Input: arr = [5]
Output: -1
Example 5:

Input: arr = [7,7,7,7,7,7,7]
Output: 7 

Constraints:

1 <= arr.length <= 500
1 <= arr[i] <= 500
"""


#Slow but O(1) memory
def findLucky_constantMemory(arr):
    if not arr:
        return -1
    elif len(arr)==1 and arr[0]==1:
        return 1
    elif len(arr)==1 and arr[0]!=1:
        return -1
    
    largest = -1
    for value in arr:
        if value==arr.count(value):
            if value>largest:
                largest = value
                
    return largest


def findLucky(arr):
    if not arr:
        return -1
    elif len(arr)==1 and arr[0]==1:
        return 1
    elif len(arr)==1 and arr[0]!=1:
        return -1
    
    lookup = {}
    for value in arr:
        if value in lookup:
            lookup[value] += 1
        else:
            lookup[value] = 1
            
    largest = -1   
    for key, value in lookup.items():
        if key==value:
            if key > largest:
                largest = key
    
    return largest