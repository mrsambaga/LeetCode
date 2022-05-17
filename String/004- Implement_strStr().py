"""
Implement strStr().
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
Clarification:
What should we return when needle is an empty string? This is a great question to ask during an interview.
For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

Input: haystack = "hello", needle = "ll"
Output: 2
"""

class Solution(object):
    def strStr(self, haystack, needle):
        
        for i,char in enumerate(haystack):
            if len(haystack) - i >= len(needle) :
                if haystack[i:i+len(needle)] == needle :
                    return i
                elif len(needle) == 1 and i == len(haystack)-1:
                    return -1
            else :
                return -1
              
"""
For this solution we can simply use iteration to check if the subword of haystack is equal to needle. Also, iterate only until the remaining letter in haystack 
less than the length of needle because theres no point to check afterward.
"""
