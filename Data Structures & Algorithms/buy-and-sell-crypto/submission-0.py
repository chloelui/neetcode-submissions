class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_ind, max_ind = 0, 0
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < prices[min_ind]:
                min_ind = i
            elif prices[i] > prices[min_ind]:
                max_ind = i
            if max_ind > min_ind:
                max_profit = max(max_profit, prices[max_ind] - prices[min_ind])

        return max_profit