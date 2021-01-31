"""
LINK: https://leetcode.com/problems/first-unique-character-in-a-string/

Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode"
return 2.
 
Note: You may assume the string contains only lowercase English letters.
"""


def firstUniqChar(s):
    hashmap = {}
    for char in s:
        if char in hashmap:
            hashmap[char] += 1
        else:
            hashmap[char] = 1
            
    for index, char in enumerate(s):
        if hashmap[char]==1:
            return index
        
    return -1