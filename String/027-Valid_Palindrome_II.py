"""
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example :
Input: s = "aba"
Output: true
"""

class Solution(object):
    def validPalindrome(self, s):
        if len(s)%2 == 0 :
            length = len(s)/2
        else :
            length = (len(s)//2) + 1
            
        for i in range(0,length):
            if s[i] != s[-(i+1)] :
                s1 = s[i:-(i+1)]
                if i == 0:
                    s2 = s[i+1:]
                else:
                    s2 = s[i+1:-i]
                if (s1 == s1[::-1]) or (s2 == s2[::-1]):
                    return True
                else :
                    return False
        return True
      
#Cleaner solution (by : yangshun)
class Solution(object):
    def validPalindrome(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                one, two = s[left:right], s[left + 1:right + 1]
                return one == one[::-1] or two == two[::-1]
            left, right = left + 1, right - 1
        return True
      
"""
Both solution has the same concept which is comparing the left char with the right char. If they're not the same, skip one on right for array 1 and skip one on left
for array 2. Check if one of the arrays are palindrome. If not, then its False. The clean solution use while loop and double pointer (left and right) which solve all the
problems that my solution had and make the code simpler. For example : while left < right will solve the problem of finding wheter the length is even or odd and 
using left and right pointer will solve the problem of getting non duplicate in index 0 because my solution will compare char[0] with char[-0] which will return [] 
thus must be given extra condition in my solution and make it more complex.
"""
