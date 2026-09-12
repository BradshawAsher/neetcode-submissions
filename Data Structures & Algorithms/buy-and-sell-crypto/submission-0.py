class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #sliding window
        #higehst possible profit is current_price - lowest_price seen so far
        #have a max profit var

        lowest_price = prices[0]
        max_profit = 0

        #start at 1
        for i in range(1, len(prices)):
            cur = prices[i]

            current_price = cur - lowest_price

            max_profit = max(max_profit, current_price)

            lowest_price = min(lowest_price, cur)
        
        return max_profit