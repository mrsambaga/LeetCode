"""
Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.
Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; and each cookie j has a size s[j]. 
If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content. 
Your goal is to maximize the number of your content children and output the maximum number.

Example :
Input: g = [1,2,3], s = [1,1]
Output: 1
Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3. 
And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
You need to output 1.
"""

class Solution(object):
    def findContentChildren(self, g, s):
        out,idx = 0, 0
        s = sorted(s)
        g = sorted(g)
        for child in g:
            while idx < len(s):
                if s[idx] >= child:
                    out += 1
                    idx += 1
                    break
                else :
                    idx += 1
        return out
      
"""
For this problem, we can sort both of the array so we can assign the smallest size cookies to smallest greed factor to get maximum content.
"""
