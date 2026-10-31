class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''total = 0
        l, r = 0, len(prices) - 1
        while l < r:
            total = max(total, prices[r] - prices[l])
            while r>l:
                total = max(total, prices[r] - prices[l])
                r -= 1
            l += 1
            r = len(prices) - 1
        return total
        '''
        
        res = 0
        l, r = 0, 1

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                res = max(res, profit)
            else:
                l = r
            r += 1
        return res
        
        


        