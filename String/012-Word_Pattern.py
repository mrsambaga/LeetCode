"""
Given a pattern and a string s, find if s follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

Example :
Input: pattern = "abba", s = "dog cat cat dog"
Output: true
"""

#Optimal solution (by : StefanPochmann)
class Solution(object):
    def wordPattern(self, pattern, str):
        s = pattern
        t = str.split()
        return len(set(zip(s, t))) == len(set(s)) == len(set(t)) and len(s) == len(t)
      
"""
This problem has similar solution like the isomorphic problem. Basically, we can map pattern to string with zip. Then, use set to eleminate the duplicate. Check if
the length is the same as set of pattern and set of splitted string. Set is used to eliminate duplicate mapping because the only thing that make it not match the pattern
is if the pattern has duplicate but the string doesnt have duplicate and vice versa. At the same time, check if pattern and splitted has the same length. Becuase 
They could have the same mapping but different length which make it not match.
"""
        

