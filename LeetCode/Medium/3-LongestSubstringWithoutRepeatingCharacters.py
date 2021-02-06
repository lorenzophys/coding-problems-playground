"""
LINK: https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Example 4:

Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""


def lengthOfLongestSubstring(s):
    start, end = 0, 0
    longest = 0
    hashset = set()
    
    while start<len(s) and end<len(s):
        if s[end] in hashset:
            hashset.remove(s[start])
            start += 1
        else:
            hashset.add(s[end])
            end += 1
            longest = max(longest, end-start)
            
    return longest