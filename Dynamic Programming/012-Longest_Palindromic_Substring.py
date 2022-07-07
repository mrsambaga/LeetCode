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
        if len(s) < 2:
            return s
        else :
            for i in range(len(s)):
                for l in range(i, len(s)):
                    temp = s[i:l]
                    if temp == temp[::-1] and len(temp) > len(longest):
                        longest = temp
            return longest
      
#Optimal Solution (By Chomolungma) :
class Solution:
    def longestPalindrome(self, s):
        if len(s)==0:
        	return 0
        maxLen=1
        start=0
        for i in range(len(s)):
        	if i-maxLen >=1 and s[i-maxLen-1:i+1]==s[i-maxLen-1:i+1][::-1]:
        		start=i-maxLen-1
        		maxLen+=2
        		continue

        	if i-maxLen >=0 and s[i-maxLen:i+1]==s[i-maxLen:i+1][::-1]:
        		start=i-maxLen
        		maxLen+=1
        return s[start:start+maxLen]

"""
The brute force solution will be O(n^2) because it check all of the combination possibilities in the string. The optimal solution is using the previous computation of
palindrome to get O(n) solution. Basically, we can find palindrome substring and then check if the substring still palindrome if we add 1 new character. This is based
on the fact that a substring will increase the length of max palindrome by only 1 or 2 if we add 1 character to a the string.
"""
