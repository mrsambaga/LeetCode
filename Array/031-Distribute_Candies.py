"""
Alice has n candies, where the ith candy is of type candyType[i]. Alice noticed that she started to gain weight, so she visited a doctor.
The doctor advised Alice to only eat n / 2 of the candies she has (n is always even). Alice likes her candies very much, and she wants to eat the maximum number of different types of candies while still following the doctor's advice.
Given the integer array candyType of length n, return the maximum number of different types of candies she can eat if she only eats n / 2 of them.

Example :
Input: candyType = [1,1,2,2,3,3]
Output: 3
Explanation: Alice can only eat 6 / 2 = 3 candies. Since there are only 3 types, she can eat one of each type.
"""

#Solution 1 (Brute force) :
class Solution(object):
    def distributeCandies(self, candyType):
        ans = []
        for x in candyType:
            if x not in ans:
                ans.append(x)
            if len(ans) == len(candyType)/2 :
                break
        return len(ans)
      
#Solution 2 (using set) :
class Solution(object):
    def distributeCandies(self, candyType):
        candy = set(candyType)
        if len(candyType)/2 < len(candy):
            return len(candyType)/2
        else :
            return len(candy)
          
"""
For this problem, the best solution is to use set to remove any duplicate in candy type. We can return the length of set if the length is less than the maximum number 
of candy type allowed, else we return the maximum number allowed.
"""
