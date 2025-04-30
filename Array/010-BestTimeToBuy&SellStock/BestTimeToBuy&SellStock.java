class Solution {
    public int maxProfit(int[] prices) {
        int maxProfit = 0;
        int buy = prices[0];

        for (int i=1; i<prices.length; i++) {
            buy = Math.min(buy, prices[i]);

            maxProfit = Math.max(maxProfit, prices[i]-buy);
        }

        return maxProfit;
    }
}

// This problem is very straightforward, we can just do one iteration to simultanously check if current stock is cheaper, if so then we buy it.
// If today profit is higher than max profit, we update the max profit.
// This solution has O(n) time complexity (full iteration once) and O(1) space complexity (storing 2 variables)
