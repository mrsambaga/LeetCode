"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example :
Input: s = "leetcode"
Output: 0
"""

#Solution 1 :
class Solution(object):
    def firstUniqChar(self, s):
        for i,char in enumerate(s):
            if s.count(char) == 1:
                return i
        return -1
      
#Optimal Solution (by : gregs) :
class Solution(object):
    def firstUniqChar(self, s):
        letters='abcdefghijklmnopqrstuvwxyz'
        index=[s.index(l) for l in letters if s.count(l) == 1]
        return min(index) if len(index) > 0 else -1
      
"""
For this solution its faster to find the index of all alphabet from a-z in the string if it appeared once, then choose the minimum from all of the index  rather than 
counting all the characters in string.
"""
