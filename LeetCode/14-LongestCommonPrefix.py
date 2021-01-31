"""
LINK: https://leetcode.com/problems/longest-common-prefix/

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings. 

Constraints:

0 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
"""


def longestCommonPrefix(strs):
    solution = ''
    
    if not strs:
        return solution
    else:
        first = strs[0]
        rest = strs[1:]
    
    for index, char in enumerate(first):
        for string in rest:
            if index>=len(string) or char!=string[index]:
                return solution
        solution += char
            
    return solution
                