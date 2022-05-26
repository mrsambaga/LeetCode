"""
Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

Example:
Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.
"""

#Optimal solution (by : rsrs3)
class Solution(object):
    def repeatedSubstringPattern(self, s):
        if not s:
            return False
            
        ss = (s + s)[1:-1]
        return ss.find(s) != -1
      
"""
This solution is very clever. Basically, a rotated string can be checked by checking if a string is exist in rotated string + rotated string. Example : 'llohe' is rotated
string of 'hello'. If we want to make sure, we can check if 'hello' is in 'llohellohe'. Turns out it is. By using this concept, we can check if a string is a repeated
string by checking if it is equal to the rotation of itself by k times. So, we remove the first and last letter to avoid getting matched by default and check if string is in string+string[1:-1]. 
"""


