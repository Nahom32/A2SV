class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        if len(prices) <=1:
            return 0
        val = prices[1:]
        d=max(prices[1:])
        big = (prices.index(d),d)
        m = big[1] - prices[0]
        for i,j in enumerate(prices):
            if i > big[0]:
                x = prices[i:]
                v = max(x)
                big = (prices.index(v),max(x))
            
            if m < big[1] - prices[i]:
                  m = big[1] - prices[i]
        if m > 0:
            return m
        else:
            return 0
        '''
        left = 0 #Buy
        right = 1 #Sell
        max_profit = 0
        while right < len(prices):
            currentProfit = prices[right] - prices[left] #our current Profit
            if prices[left] < prices[right]:
                max_profit =max(currentProfit,max_profit)
            else:
                left = right
            right += 1
        return max_profit
        
                
            
            
        
            
        