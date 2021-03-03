"""
LINK: https://leetcode.com/problems/kth-largest-element-in-an-array/

Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5

Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""


def findKthLargest(nums, k):
    length = len(nums)
    root = length // 2
    
    for i in range(root, -1, -1):
        heapify(nums, length, i)
        
    for i in range(length-1, length-k, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)
        
    return nums[0]

def heapify(nums, length, root):
    largest = root
    left = 2 * root + 1
    right = 2 * root + 2
    
    if left<length and nums[left]>nums[largest]:
        largest = left
    if right<length and nums[right]>nums[largest]:
        largest = right
        
    if largest!=root:
        nums[root], nums[largest] = nums[largest], nums[root]
        heapify(nums, length, largest)



import heapq 

def findKthLargest_heapq(nums, k):
    length = len(nums)
    heapify(nums)
    
    for _ in range(length-k):
        heappop(nums)
        
    return nums[0]