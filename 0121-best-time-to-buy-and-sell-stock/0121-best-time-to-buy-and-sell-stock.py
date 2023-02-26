class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxp = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxp = max(profit, maxp)
            else:
                l = r
            r += 1
        return maxp

    def _ntime_constant_space(self, a: List[int]) -> "[sellday,buyday,work]":
        left=0
        right=1
        work=0
        maxprofit=0
        sellday,buyday=0,0
        while right < len(a):
            work+=1
            if a[left] < a[right]:
                profit=a[right]-a[left]
                if profit > maxprofit:
                    buyday=left
                    sellday=right
                    maxprofit=profit
            else:
                left=right
            right=right+1
        sol=[sellday,buyday,work]
        return sol
