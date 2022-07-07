"""
Given a string s, return the longest palindromic substring in s.

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
"""

#Solution 1 (Brute Force) :
class Solution(object):
    def longestPalindrome(self, s):
        longest = ""
        for i in range(len(s)):
            for l in range(i, len(s)+1):
                temp = s[i:l]
                if temp == temp[::-1] and len(temp) > len(longest):
                    longest = temp
        return longest
      
#Optimal Solution :
