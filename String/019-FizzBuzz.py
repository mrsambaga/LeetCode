"""
Given an integer n, return a string array answer (1-indexed) where:
answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.

Example:
Input: n = 3
Output: ["1","2","Fizz"]
"""

class Solution(object):
    def fizzBuzz(self, n):
        ans = []
        for i in range(1,n+1):
            if i % 3 == 0 and i % 5 == 0:
                ans.append('FizzBuzz')
            elif i % 3 == 0:
                ans.append('Fizz')
            elif i % 5 == 0:
                ans.append('Buzz')
            else :
                ans.append(str(i))
        return ans
      
#One liner solution with string multiplication (by : StefanPochmann)
class Solution(object):
    def fizzBuzz(self, n):
        return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n+1)]
      
"""
This problem is pretty simple. We can just use modulo operator to check if number is divisible by something. The one liner solution use multiplication by multiplying
the 'Fizz', 'Buzz', or both with boolean of modulo operator. This can be done because in python if string multiplied by 0 it will become "" and if it multiplied by 1
the result will be itself.
"""
