"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example :
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
"""

class Solution(object):
    def generateParenthesis(self, n):
        dp = [[] for i in range(n + 1)]
        dp[0].append('')
        for i in range(n + 1):
            for j in range(i):
                dp[i] += ['(' + x + ')' + y for x in dp[j] for y in dp[i - j - 1]]
        return dp[n]
      
