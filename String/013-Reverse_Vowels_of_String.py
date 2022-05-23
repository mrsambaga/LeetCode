"""
Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.

Input: s = "hello"
Output: "holle"
"""

#Solution 1 with for loops
class Solution(object):
    def reverseVowels(self, s):
        s = list(s)
        vowels = []
        for i in s:
            if i in 'aiueoAIUEO':
                vowels.append(i)
        for i in range(len(s)):
            if s[i] in 'aiueoAIUEO':
                s[i] = vowels.pop()
        return ''.join(s)
      
#Optimal solution with regex (by: StefanPochmann)
def reverseVowels(self, s):
    vowels = re.findall('(?i)[aeiou]', s)
    return re.sub('(?i)[aeiou]', lambda m: vowels.pop(), s)
  
"""
For solution 1, i use iteration to track all vowels in string and use another iteration to reverse them by using pop. For optimal solution, we can use regex to find
all vowels in s with findall, then change them with sub & pop() to reverse the vowels.
"""
