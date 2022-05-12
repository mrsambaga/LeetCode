"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example :
Input: strs = ["flower","flow","flight"]
Output: "fl"
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        ans = []
        maximum = list(max(strs, key=len))
        for i,letter in enumerate(maximum):
            for y in strs:
                y = list(y)
                if i+1 > len(y) or y[i] != letter :
                    curr_prefix = ""
                    break
                else :
                    curr_prefix = letter
            if curr_prefix :
                ans.append(curr_prefix)
            else :
                break
        return "".join(ans)
      
"""
The solution of this problem mostly is a brute force solution where we need to search and do 2 iteration. We can check one by one the letter of the longest word with
every letter in the array. If they stop being the same, stop the entire program. From looking at the disscussion, changing the maximum to minimum word and only iterate
that many letter will simplify the entire code but with the same time complexity.
"""
      
