class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price=prices[0]
        profit=0
        sum=0

        for i in range(0,len(prices)):
            min_price=min(min_price, prices[i])
            profit=max(profit, prices[i]-min_price)
            if i+1<len(prices) and prices[i+1]<prices[i]:
                sum += profit
                min_price=prices[i+1]
                profit=0

        sum = sum + profit
        return sum

s=Solution()
print(s.maxProfit(prices = [7,1,5,3,6,4]))
