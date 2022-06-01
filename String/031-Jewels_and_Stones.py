"""
You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.
Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example :
Input: jewels = "aA", stones = "aAAbbbb"
Output: 3
"""

class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        ans = 0
        for ch in jewels:
            ans += stones.count(ch)
        return ans
      
class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        return sum(map(jewels.count, stones))
      
"""
For this problem, we can just count how many letters in jewels that are also in stones.
"""
