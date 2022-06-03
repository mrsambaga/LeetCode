"""
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.
Note that after backspacing an empty text, the text will continue empty.

Example :
Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
"""

class Solution(object):
    def backspaceCompare(self, s, t):
        del_s, del_t = [], []
        i, m = 0,0
        while i < len(s) or m < len(t):
            if i < len(s):
                if s[i] != '#' :
                    del_s.append(s[i])
                elif s[i] == '#' and del_s != []:
                    del_s.pop()
            if m < len(t):
                if t[i] != '#' :
                    del_t.append(t[i])
                elif t[i] == '#' and del_t != []:
                    del_t.pop()
            i += 1
            m += 1
        return del_s == del_t
      
#Optimal Solution (by : lee215) :
class Solution(object):
    def backspaceCompare(self, S, T):
        back = lambda res, c: res[:-1] if c == '#' else res + c
        return reduce(back, S, "") == reduce(back, T, "")
      
"""
For this problem, we can use stack algorithm where we append new character if its not # and pop the list if its #. We can simplify this code with reduce() function
as we can see in optimal solution. Reduce will apply function for every element in a list(in this case string). It also has "" as 3rd attribute to deal with # in the
beginning.
"""
