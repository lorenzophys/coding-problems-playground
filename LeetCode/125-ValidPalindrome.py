"""
LINK: https://leetcode.com/problems/valid-palindrome/

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true

Example 2:

Input: "race a car"
Output: false 

Constraints:

s consists only of printable ASCII characters.
"""


def isPalindrome_while(s):
    s=s.translate(str.maketrans('', '', string.punctuation)).lower().replace(' ','')
    start, end = 0, len(s) - 1
    
    while start<=end:
        if s[start]==s[end]:
            start += 1
            end -= 1
        else:
            return False
        
    return True


def isPalindrome_for(s):
    s=s.translate(str.maketrans('', '', string.punctuation)).lower().replace(' ','')
    end = len(s) - 1

    for start in range(len(s)):
        if s[start]==s[end]:
            end -= 1
        else:
            return False
        
    return True


def isPalindrome_twoLines(s):
    s=s.translate(str.maketrans('', '', string.punctuation)).lower().replace(' ','')
    
    return s == s[::-1]