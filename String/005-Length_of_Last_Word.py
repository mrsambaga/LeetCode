"""
Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.

Example :
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
"""

class Solution(object):
    def lengthOfLastWord(self, s):
        return len(s.split()[-1])

#Better solution (by DBabichev)
class Solution:
    def lengthOfLastWord(self, s):
        end = len(s) - 1
        while end > 0 and s[end] == " ": end -= 1
        beg = end
        while beg >= 0 and s[beg] != " ": beg -= 1
        return end - beg
      
"""
This problem is pretty simple in Python. We can use split to strip all space (including trailing & leading) and put all word into array then check the length of last array.
Another solution can be done by checking the word backwards from the end. First we check for trailing spaces and then mark the end as soon as we find a letter.
Then check all letter going backward until we meet a space again, then mark the begining before we meet a space. Finally, find the length by subtracting the end with the
begining.
"""
