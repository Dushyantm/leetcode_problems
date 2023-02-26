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


    def _nlogn_time_logn_space(self, a: List[int]) -> "[sellday,buyday,work]":
       
        a = self.divide_n_conquer(a, 0, len(a)-1)
        
        sell_day = a[2]
        buy_day = a[1]
        work = a[0]
        return [sell_day, buy_day, work]
    
    def divide_n_conquer(self, arr, start, stop):
        n = stop - start

        if n == 0:
            return 0, start, start

        if n == 1:
            return arr[stop] - arr[start], start, stop

        mid = int(start + n/2)

        max_profit_left, buy_left, sell_left = self.divide_n_conquer(arr, start, mid-1)
        max_profit_right, buy_right, sell_right = self.divide_n_conquer(arr, mid, stop)

        buy_index = start
        mp_buy_val = arr[start]
        for k in range(start+1, mid):
            if arr[k] < mp_buy_val:
                mp_buy_val = arr[k]
                buy_index = k

        sell_index = mid
        mp_sell_val = arr[mid]
        for k in range(mid+1, stop+1):
            if arr[k] > mp_sell_val:
                mp_sell_val = arr[k]
                sell_index = k

        max_profit_ttl = mp_sell_val - mp_buy_val

        if max_profit_right > max_profit_left:
            if max_profit_ttl > max_profit_right:
                return max_profit_ttl, buy_index, sell_index
            else:
                return max_profit_right, buy_right, sell_right
        else:
            if max_profit_ttl > max_profit_left:
                return max_profit_ttl, buy_index, sell_index
            else:
                return max_profit_left, buy_left, sell_left