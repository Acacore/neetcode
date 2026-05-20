class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_price = 0
        profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                current_profit = price - min_price
                if profit < current_profit:
                    profit = current_profit
        return profit


        
        