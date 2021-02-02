"""
LINK: https://leetcode.com/problems/palindrome-number/


"""


def isPalindrome(x):
    if x<0:
        return False

    reversed = 0
    original = x

    while x!=0:
        reversed = reversed*10 + x%10
        x//=10

    return reversed==original


def isPalindrome_convertToString(x):
    if x<0:
        return False
    
    return x == int(str(x)[::-1])