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
        s = list(''.join(s.lower().split()))
        ans = [letter for letter in s if letter.isalnum()]
        
        if ''.join(ans) == ''.join(ans[::-1]) :
            return True
        else :
            return False
          
"""
For this problem we can do a couple of steps before we check if the sentence is palindrom. Those steps are remove spaces with split(), lowercase the sentence with lower(),
and then include only alphanumeric with isalnum() condition. After that, we can check if the sentence is palindrome using backward indexing.
"""
