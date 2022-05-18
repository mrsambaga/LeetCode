"""
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...

Input: columnNumber = 1
Output: "A"
"""

#Clear solution (by : yuzhiqiang)
class Solution:
    def convertToTitle(self, columnNumber):
        capitals = [chr(x) for x in range(ord('A'), ord('Z')+1)]
        result = []
        while columnNumber > 0:
            result.append(capitals[(columnNumber-1)%26])
            columnNumber = (columnNumber-1) // 26
        result.reverse()
        return ''.join(result)
      
"""
For this problem we could check the modulo 26 of the columNumber in every iteration and append it to the result. Then, do floor division of columnNumber to move to the
next character (if any) like ZZZ or AAAA. We can do this because the formula of excel title format is !26^n with n equal to the number of character. So, if there is
4 character (ZZZZ) then the number is 26 + 26^2 + 26^3  + 26^4 = 475254. We could find the total number of character by iterating a floor division on columnNumber 
"""
