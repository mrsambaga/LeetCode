"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

Example :
Input: s = "III"
Output: 3
Explanation: III = 3.
"""

class Solution(object):
    def romanToInt(self, s):
        roman = {"I" : 1, "V" : 5, "X" : 10, "L" : 50,  "C" : 100, "D" : 500, "M" : 1000}
        s = list(s)
        ans = roman[s[len(s)-1]]
        for i in range(2, len(s)+1) :
            if (s[-i] == "I" and s[-i+1] in ["V","X"]) or (s[-i] == "X" and s[-i+1] in ["L","C"]) or (s[-i] == "C" and s[-i+1] in ["D","M"]) :
                ans -= roman[s[-i]]
            else :
                ans += roman[s[-i]]
        return ans
      
"""
There are a lot of way to solve this proble, one of them is to iterate from behind and check if a certain character appear before character. If yes then it subtract
the total by that character. If no, then add it to total.
"""
