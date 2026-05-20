class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for price in prices:
            profit = price - min_price

            if profit > max_profit:
                max_profit = profit

            if price < min_price:
                min_price = price

        return max_profit
## take first number as minimum buying price
#take maximum profit as 0 
#traverse array from right to left 
#calculate today's profit 
#if profit is bigger then update max_profit 
#if current price is smaller then update the price  

