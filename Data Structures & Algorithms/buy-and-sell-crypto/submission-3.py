class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0 

        

        minPrice = 999999

        for p in prices:

            if p<minPrice:
                minPrice = p 

            profit = p - minPrice

            maxProfit = max(maxProfit,profit)

        return maxProfit if maxProfit >0 else 0




        
       


            
        