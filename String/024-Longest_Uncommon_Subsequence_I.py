"""
Given two strings a and b, return the length of the longest uncommon subsequence between a and b. If the longest uncommon subsequence does not exist, return -1.
An uncommon subsequence between two strings is a string that is a subsequence of one but not the other.
A subsequence of a string s is a string that can be obtained after deleting any number of characters from s.
For example, "abc" is a subsequence of "aebdc" because you can delete the underlined characters in "aebdc" to get "abc". Other subsequences of "aebdc" include "aebdc", "aeb", and "" (empty string).

Example :
Input: a = "aba", b = "cdc"
Output: 3
Explanation: One longest uncommon subsequence is "aba" because "aba" is a subsequence of "aba" but not "cdc".
Note that "cdc" is also a longest uncommon subsequence.
"""

class Solution(object):
    def findLUSlength(self, a, b):
        if a != b:
            return max(len(a), len(b))
        else :
            return -1
          
"""
This problem actually make me overthink with all those explanations and problem statement. Actually, we just need to find the maximum length between a and b because
the maximum subsequence is either a or b if a is not equal to b. If they are equal, they dont have any subsequence.
"""
