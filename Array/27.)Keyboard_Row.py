"""
Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.
In the American keyboard:
the first row consists of the characters "qwertyuiop",
the second row consists of the characters "asdfghjkl", and
the third row consists of the characters "zxcvbnm".

Input: words = ["Hello","Alaska","Dad","Peace"]
Output: ["Alaska","Dad"]
"""

class Solution(object):
    def findWords(self, words):
        Row1 = ['q','w','e','r','t','y','u','i','o','p']
        Row2 = ['a','s','d','f','g','h','j','k','l']
        Row3 = ['z','x','c','v','b','n','m']
        ans = []
        
        for x in words:
            y = list(x.lower())
            if set(y) <= set(Row1):
                ans.append(x)
            elif set(y) <= set(Row2):
                ans.append(x)
            elif set(y) <= set(Row3):
                ans.append(x)
        return ans
      
"""
For this problem, we can check if the list of word is a subset of any row by using set(). If true, then it can be typed by same line characters. This problem can also
use issubset() to check if list is a subset of another list.
"""
