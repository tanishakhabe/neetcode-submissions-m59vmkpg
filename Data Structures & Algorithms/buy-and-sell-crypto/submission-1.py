class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0    # buy day
        r = 1   # sell day
        max_profit = 0

        while r < len(prices): 
            if prices[r] > prices[l]: 
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            else:
                l = r
            r += 1
        return max_profit


    
[10,1,5,6,7,1]

l = 5
r= 6 
mp=6