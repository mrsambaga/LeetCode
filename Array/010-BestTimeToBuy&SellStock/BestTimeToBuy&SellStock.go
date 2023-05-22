func maxProfit(prices []int) int {
    profit := 0
    buy := prices[0]
    
    for i:=1; i<len(prices); i++ {
        if prices[i] - buy > profit {
            profit = prices[i] - buy
        } else if prices[i] < buy {
            buy = prices[i]
        }
    }
    
    return profit
}
