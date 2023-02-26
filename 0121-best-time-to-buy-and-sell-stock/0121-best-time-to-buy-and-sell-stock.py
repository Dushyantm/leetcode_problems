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


    def nsquare_time_constant_space(self, a: List[int]) -> "[sellday,buyday,work]":
            n = len(a)
            buyday = sellday = 0
            work = profit = 0
            for i in range(n):
                for j in range(i, n):
                    if a[j] - a[i] > profit:
                        profit = a[j] - a[i]
                        buyday, sellday = i, j
                    work += 1
            sol =[sellday, buyday, work]
            return sol
        