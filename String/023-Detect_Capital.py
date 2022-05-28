"""
We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Given a string word, return true if the usage of capitals in it is right.

Example :
Input: word = "USA"
Output: true
"""

class Solution(object):
    def detectCapitalUse(self, word):
        if word.isupper() == True:
            return True
        elif word.islower() == True:
            return True
        elif word[0].isupper() == True:
            for char in word[1:] :
                if char.isupper() == True:
                    return False
            return True
        else :
            return False
          
#Optimal solution (by : StefanPochmann) :
def detectCapitalUse(self, word):
    return word.isupper() or word.islower() or word.istitle()
  
"""
I never know there's method called istitle() in Python which return True is the first char of word is capital and the rest is lowercase.
"""
