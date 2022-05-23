"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.

Example :
Input: ransomNote = "a", magazine = "b"
Output: false
"""

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        ransomNote = list(ransomNote)
        for x in magazine:
            if x in ransomNote :
                ransomNote.remove(x)
        return ''.join(ransomNote) == ""
      
"""
For this problem, we can use iteration to check if letter in ransomNote are in magazine too then remove if everytime it found. We can also use count() in every iteration
to compare if a letter in ransomNote appeared less times than in magazine. If not, then we know its false.
"""
