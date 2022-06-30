"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative 
positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example :
Input: s = "abc", t = "ahbgdc"
Output: true
"""

class Solution(object):
    def isSubsequence(self, s, t):
        length = 0
        idx = 0
        if len(s) < 1:
            return True
        else:
            for i in range(len(t)):
                if t[i] == s[idx]:
                    length += 1
                    idx += 1
                if length == len(s):
                    return True
                  
"""
We can check if the s character is in t 1 by 1 in an iteration. Count every time we found s in t. Return true if the final count = length of s (all char found)
"""
                  
