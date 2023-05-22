"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example :
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
"""

class Solution(object):
    def maxProfit(self, prices):
        profit = 0
        buy = prices[0]
        for i in range(1, len(prices)):
            if prices[i] - buy > profit:
                profit = prices[i] - buy
            elif prices[i] < buy :
                buy = prices[i]
        
        return profit

"""
We can solve this problem using linear iteration. Basically, we can keep the price when we buy the stock outside iteration and update it whenever we see a stock
cheeper than the buy price. We can just start the iteration from the 2nd element as the sell price and use 1st element as the buy price and then subtracting 
the sell price with the buy price. 
"""
