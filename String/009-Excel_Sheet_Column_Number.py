"""
Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...

Example :
Input: columnTitle = "A"
Output: 1
"""

class Solution(object):
    def titleToNumber(self, columnTitle):
        letter = [chr(x) for x in range(ord('A'), ord('Z')+1)]
        num = [x for x in range(1,27)]
        z = dict(zip(letter,num))
        multiplier = 1
        ans = 0
        
        for i in list(columnTitle)[::-1]:
            ans += multiplier * z[i]
            multiplier *= 26
        return ans
      
"""
By solving the last problem, we already know the formula of characters to numbers conversion. The formula is 26^!n-1 * character conversion (A=1, B=2 etc) 
where n = number of character. For characters "ZZZZ" it can be written as 26^3 * 26 + 26^2 * 26 + 26^1 * 26 + 26^0 * 26 = 475254 and 
"AAA" equal to 26^2 * 1 + 26^1 * 1 + 26^0 * 1 = 703
"""

