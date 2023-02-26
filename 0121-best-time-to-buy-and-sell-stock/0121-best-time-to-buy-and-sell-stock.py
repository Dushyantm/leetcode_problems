class Solution:
    def __init__(self):
        self.work = 0
        pass
        ## YoU can have what ever you want here
        

    ##LEETCODE INTERFACE.  DO NOT CHANGE
    ## YOU CANNOT CHANGE ANYTHING
    def maxProfit(self, prices: List[int]) -> int:
        if False:
            [sellday, buyday, work] = self.nsquare_time_constant_space(prices)
        if False:
            [sellday, buyday, work] = self.nlogn_time_logn_space(prices)
        if True:
            [sellday, buyday, work] = self.ntime_constant_space(prices)
        p = self._compute_profit(prices, sellday, buyday)
        return p

    #############################################
    # All public function here. 
    #############################################

    ########################################
    # TIME:THETA(N^2)
    # Space:THETA(1)
    # CANNOT CHANGE ANYTHING BELOW
    #########################################
    def nsquare_time_constant_space(self, a: List[int]) -> "[sellday,buyday,work]":
        return self._nsquare_time_constant_space(a) 


    ########################################
    # TIME:THETA(NlogN)
    # Space:THETA(logn)
    # CANNOT CHANGE ANYTHING BELOW
    #########################################
    def nlogn_time_logn_space(self, a: List[int]) -> "[sellday,buyday,work]":
        return self._nlogn_time_logn_space(a)

    ########################################
    # TIME:THETA(N)
    # Space:THETA(1)
    # CANNOT CHANGE ANYTHING BELOW
    #########################################
    def ntime_constant_space(self, a: List[int]) -> "[sellday,buyday,work]":
        return self._ntime_constant_space(a)
        

    #############################################
    # All private function here. 
    # WRIYE CODE BELOW
    # You can have any number of private functions and variables
    # NOTHING CAN BE CHABGED BELOW
    #############################################
    def _compute_profit(self, a: List[int], s: "int", b: "int") -> "int":
        n = len(a)
        if n == 0:
            return 0
        assert s >= 0 and s < n
        assert b >= 0 and b < n
        assert s >= b
        p = a[s] - a[b]
        return p

    

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