class Solution:
    def maxProfit(self, prices: List[int]) -> int:



        min_price = float("inf")
        max_profit = -float("inf")

        for price in prices:

            if price < min_price:
                min_price = price
            if (price - min_price) > max_profit:
                max_profit = price - min_price

            print(max_profit)

        return max_profit

        