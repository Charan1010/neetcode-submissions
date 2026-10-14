class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        min_price = float('inf')
        profit = -float('inf')

        for price in prices:

            if price < min_price:
                min_price = price

            if (price - min_price) > profit:
                profit = price - min_price

        return profit

        