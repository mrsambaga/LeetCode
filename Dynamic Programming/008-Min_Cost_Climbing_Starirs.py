"""
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.
You can either start from the step with index 0, or the step with index 1.
Return the minimum cost to reach the top of the floor.

Example:

Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
"""

#Optimal solution by : (pccisme)
class Solution(object):
    def minCostClimbingStairs(self, cost):
        if not cost:
            return 0
        out = [0] * len(cost)
        out[0], out[1] = cost[0], cost[1]
        for i in range(2,len(cost)):
            out[i] = cost[i] + min(out[i-2],out[i-1])
        return min(out[-2],out[-1])
      
"""
Based on the optimal solution, we can solve this problem by counting all cost to reach the n-th stairs. First we declare the 0th and 1st step is equal to the cost
of 1st and 0th stair because they have no preceding cost. Then, for every step, we check if the cost to reach that stair is cheaper by walking from the previous
1 stair or previous 2 stair then put the cheapest one. Do it till all the stairs calculated. Then, compare the last 1 and last 2 cost of stairs and find the cheapest one.
Because the last 1 and last 2 stair will equally take 1 more step (1 or 2 stair) in order to finish the staircase.
"""
