"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Input: s = "()"
Output: true
"""

#Simple solution using stack (by xiaoying10101)

class Solution(object):
    def isValid(self, s):
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []
      
"""
This solution can be solved using stack to track every open parentheses and store them in an array. If we meet a close parentheses, check if the last open parentheses
is match or if stack is not empty. If false then the string is invalid because it might has single open parentheses in between different parentheses or string contain
only closing parentheses/open parentheses.
"""
       
