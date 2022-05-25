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
        i = 0
        for char in t:
            if i < len(s) :
                if char == list(s)[i]:
                    i += 1
            else :
                return True
        return i == len(s)
      
"""
Since subsequence strings is a string contained in another larger string with the same relative position of characters, we can solve this problem with O(n) time 
complexity by checking the characters 1 by 1 with iteration. If the character match the subsequence string character, go next and repeat it until the larger string is
covered or all characters has been found. If not all characters is found, then the string is not subsequence.
"""
