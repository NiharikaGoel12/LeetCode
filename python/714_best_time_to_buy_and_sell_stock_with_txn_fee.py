class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        current_price=prices[0] #1
        total_profit = 0
        profit=0

        for i in range(0, len(prices)):
            current_price=min(current_price, prices[i])
            profit = max(profit, prices[i]- current_price -fee)
            if i+1<len(prices) and prices[i+1]<(prices[i] + fee):
               
                    total_profit+=profit
                    current_price=prices[i]
                    profit = 0

        return total_profit + profit

s=Solution()
print(s.maxProfit(prices = [1,3,2,8,4,9], fee = 2))
print(s.maxProfit(prices = [1,3,7,5,10,3], fee = 3))