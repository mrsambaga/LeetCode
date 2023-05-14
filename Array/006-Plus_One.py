"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.

Example :
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
"""

class Solution(object):
    def plusOne(self, digits):
        temp = ''
        for i in digits : 
            temp += str(i)
        digits = int(temp) + 1    
        return list(str(digits))
    
# Faster way ( log(n) time complexity)

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 0
        digits[len(digits)-1] += 1
        if digits[len(digits)-1] > 9 :
            digits[len(digits)-1] = 0
            carry += 1

        for i in range(len(digits)-2, -1, -1):
            if digits[i] + carry > 9 :
                digits[i] = 0
                carry = 1
            else :
                digits[i] = digits[i] + carry
                carry = 0
                    
        if carry > 0:
            digits[0] = 1
            digits.append(0)
        
        return digits

"""
For this problem we can convert the digits into string and concatenate them through iteration. Then, convert them into integer so it can be incremented by 1.
Last, convert it back to string so it can be made into list.
"""
