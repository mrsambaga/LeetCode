"""
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
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        strMap = {}
        left = 0
        longest = 0
        
        for right in range(len(s)):
            while s[right] in strMap:
                del strMap[s[left]]
                left += 1
            strMap[s[right]] = True
            longest = max(longest, right - left + 1)
        return longest
      
"""
For this problem, we can use sliding window & hash map for optimal solution. If we meet a duplicate character, we can move the left pointer
to the right by + 1 (slide the substring window to the right) until the duplicate characters is gone. Then, we count the length of window
and store the maximum everytime we add a new character.
"""
