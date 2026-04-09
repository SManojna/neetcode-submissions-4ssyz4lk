class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP =  0 
        minBuy = prices[0]
        for p in prices:
            pro = p - minBuy
            maxP = max(maxP, pro)
            minBuy = min(minBuy,p)
        return maxP
        