class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        bestprice = 0
        for right in range(1,len(prices)):
            if prices[left] < prices[right]:
                best = prices[right]-prices[left]
                bestprice = max(bestprice,best)
            else:
                left = right
        return bestprice


