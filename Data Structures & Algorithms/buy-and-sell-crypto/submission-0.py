class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # choose lowest day to buy
        # choose highest day after lowest day to sell
        # return max profit
        # or if no profit, return 0:
            # case when prices is descending or buy and sell price are the same

        left, right = 0, 1
        max_profit = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                max_profit =max(max_profit, prices[right] - prices[left])
            else:
                left = right
            right += 1

        return max_profit


 