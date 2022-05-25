"""
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

Example :
Input: s = "abccccdd"
Output: 7
Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
"""

class Solution(object):
    def longestPalindrome(self, s):
        characters = {}
        ans = 0
        odd = 0
        for x in s:
            if x not in characters.keys():
                characters[x] = 1
            else :
                characters[x] += 1
        for key in characters.keys():
            if characters[key] % 2 == 0:
                ans += characters[key]
            elif characters[key] % 2 == 1:
                ans += characters[key] - 1
                odd += 1
        if odd > 0 :
            return ans + 1
        else :
            return ans
          
#Optimal Solution (by : StefanPochmann)
class Solution(object):
    def longestPalindrome(self, s):
        odds = sum(v & 1 for v in collections.Counter(s).values())
        return len(s) - odds + bool(odds)
      
"""
For my original solution, i was trying to map every characters in dictionary so i can see which one appeared even times and odd times. Then, i add every characters
that appeared even times, and appeared odd times - 1, and + 1. This is because we can only keep 1 character that are odd so i subtract the odd by 1 so it become even
and add 1 at the end for 1 character. Turns out, this can be done much simpler in optimal solution. We dont have to care with even character and just count how many
character that appeared odd times and subtract the length of string by that number. This represent the subtraction of odd char by 1 in every iteration. 
Last, make bool(odd) so it will add 1 if there is odd character or 0 if the is no odd character.
"""
