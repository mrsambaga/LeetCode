"""
You are given an integer n. A 0-indexed integer array nums of length n + 1 is generated in the following way:
nums[0] = 0
nums[1] = 1
nums[2 * i] = nums[i] when 2 <= 2 * i <= n
nums[2 * i + 1] = nums[i] + nums[i + 1] when 2 <= 2 * i + 1 <= n
Return the maximum integer in the array nums.

Example:
Input: n = 7
Output: 3
Explanation: According to the given rules:
  nums[0] = 0
  nums[1] = 1
  nums[(1 * 2) = 2] = nums[1] = 1
  nums[(1 * 2) + 1 = 3] = nums[1] + nums[2] = 1 + 1 = 2
  nums[(2 * 2) = 4] = nums[2] = 1
  nums[(2 * 2) + 1 = 5] = nums[2] + nums[3] = 1 + 2 = 3
  nums[(3 * 2) = 6] = nums[3] = 2
  nums[(3 * 2) + 1 = 7] = nums[3] + nums[4] = 2 + 1 = 3
Hence, nums = [0,1,1,2,1,3,2,3], and the maximum is max(0,1,1,2,1,3,2,3) = 3.
"""

class Solution(object):
    def getMaximumGenerated(self, n):
        if n < 2:
            return n
        else :
            nums = [0,1] + [0]*(n-1)
            for i in range(2,n+1):
                if i%2 == 0:
                    nums[i] = nums[i/2]
                elif i%2 == 1:
                    nums[i] = nums[(i-1)/2] + nums[(i+1)/2]
            return max(nums)

"""
This problem basically calculate odd and even element with different pattern. We can revese odd and even requirement to get the formula ex: nums[2 * i] = nums[i] if
we put nums[2*i] -> nums[x] we can check if x%2 = 0 to check if the criteria is met. If true, then nums[x] = nums[x/2] (the reverse formula). Do it again for the odd
formula.
"""


