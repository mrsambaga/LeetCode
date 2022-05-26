"""
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.
You must solve the problem without using any built-in library for handling large integers (such as BigInteger). 
You must also not convert the inputs to integers directly

Example :
Input: num1 = "11", num2 = "123"
Output: "134"
"""

class Solution(object):
    def addStrings(self, num1, num2):
        num1, num2 = list(num1), list(num2)
        multiplier = 1
        ans = 0
        
        while num1 or num2 :
            if num1:
                ans += (ord(num1.pop())-ord('0')) * multiplier
            if num2:
                ans += (ord(num2.pop())-ord('0')) * multiplier
                
            multiplier *= 10
        return str(ans)
      
"""
For this problem, we can use ord() to find the numerical representation of a string. We subtract it with ord('0') to get the same number as represented. Example :
ord('7') = 55 but ord('7')-ord('0') = 7. Dont forget to use multiplier because every number from right will increase of value in 10^n-1 with n = number from right.
We an sum it all and convert it to string in the end.
"""
