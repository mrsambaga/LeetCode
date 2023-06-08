"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

Example :
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
"""

class Solution(object):
    def isPalindrome(self, s):
        newStr = ""
        for letter in s :
            if letter.isalnum() :
                newStr += lower(letter)
        return newStr == newStr[::-1]
      
# Faster & O(1) memory solution using double pointer :

class Solution(object):
    def isPalindrome(self, s):
        startPointer = 0
        endPointer = len(s)-1
        
        while startPointer < endPointer:
            while startPointer < len(s)-1 and not s[startPointer].isalnum():
                startPointer += 1
            while endPointer >= 0 and not s[endPointer].isalnum():
                endPointer -= 1
            
            if lower(s[startPointer]) != lower(s[endPointer]):
                return False
            
            startPointer += 1
            endPointer -= 1
        return True
          
"""
For this problem we can do a couple of steps before we check if the sentence is palindrom. Those steps are remove spaces with split(), lowercase the sentence with lower(),
and then include only alphanumeric with isalnum() condition. After that, we can check if the sentence is palindrome using backward indexing.
"""
