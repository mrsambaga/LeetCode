"""
Given two binary strings a and b, return their sum as a binary string.

Example :
Input: a = "11", b = "1"
Output: "100"
"""

#Optimal solution (by : vtqq)

class Solution(object):
    def addBinary(self, a, b):
        carry = 0
        result = ''

        a = list(a)
        b = list(b)

        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())

            result += str(carry %2)
            carry //= 2

        return result[::-1]
      
"""
Since binary addition done from the back first, we could make a list and then pop every in iteration to calculate the addition. Then calculate the modulus 2 of
the addition and then put it in the result. The modulo will return just like binary addition. To track the carry, use floor division to find the largest possible result
of division. If the carry is 2,3, after floor division it will result in 1. It means the operation has 1 carry.
"""
