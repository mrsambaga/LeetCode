"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Input: s = "anagram", t = "nagaram"
Output: true
"""

#Solution 1 (using sort)
class Solution(object):
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)

#Soltion 2 (using dictionary)
class Solution(object):
    def isAnagram(self, s, t):
        dic_s, dic_t = {}, {}
        
        if len(s) != len(t) :
            return False
        else :
            for x in range(len(s)):
                if s[x] not in dic_s.keys():
                    dic_s[s[x]] = 1
                else :
                    dic_s[s[x]] += 1
                if t[x] not in dic_t.keys():
                    dic_t[t[x]] = 1
                else :
                    dic_t[t[x]] += 1 
                           
        return dic_s == dic_t
      
"""
The main goal for this problem is we have to be able to check if both string contain same combination of letter or not.
"""
