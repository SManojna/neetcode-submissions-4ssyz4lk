class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPro = 0 
        for i in range(0,len(prices)-1):
            p1 = prices[i]
            p2 = max(prices[i+1:])
            pro = p2-p1 
            maxPro = max(pro,maxPro)
        return maxPro
        