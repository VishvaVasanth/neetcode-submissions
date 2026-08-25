class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxprofit = -99999
        lowprice = prices[0]

        for price in prices:
            if lowprice==price:
                continue
            if price<lowprice:
                lowprice = price
            else:
                profit = price-lowprice
                maxprofit=max(profit,maxprofit)
        return maxprofit if maxprofit>0 else 0
            


            
        