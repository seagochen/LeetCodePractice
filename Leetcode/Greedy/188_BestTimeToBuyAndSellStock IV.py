"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

Find the maximum profit you can achieve. You may complete at most k transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Example 1:

Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.

Example 2:

Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
"""

from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        """
        Use the idea of "reinvesting", we can "carry-over" a
        previous transaction into the next transaction in order
        to calculate a total profit.
        
        For example, given [3,2,6,5,7,0,3]
                
        If k = 1, then we would keep track of the lowest price and
        max profit for each day.
        
            3, min_price [3], max_profit [0]
            2, min_price [2], max_profit [0]
            6, min_price [2], max_profit [4]
            5, min_price [2], max_profit [4]
            7, min_price [2], max_profit [5]
            0, min_price [0], max_profit [5]
            3, min_price [0], max_profit [5]
        
        If k = 2, we want to understand how much money we could make
        if we "reinvest" profit from k = 1. This means we could only
        initiate a k=2 transaction IFF k=1 (on a previous day) has a
        non-zero max_profit.
        
            3, min_price [3, 3], max_profit [0, 0]
            2, min_price [2, 2], max_profit [0, 0]
            6, min_price [2, 2], max_profit [4, 4]
            5, min_price [2, 1], max_profit [4, 4]  <- Reinvest profit
            7, min_price [2, 1], max_profit [5, 6]
            0, min_price [0, -5], max_profit [5, 6]
            3, min_price [0, -5], max_profit [5, 8] <- Max profit with 2 transactions
        
        Notice that the new min_price is $1 when price is $5. Similarly, the new min_price
        is -$5 when price is $0. Why?
                
        To understand, imagine if we bought at $2 and sold at $6. Then bought at $5
        and sold at $7. That is two transactions with a total profit of
        $4 + $2 = $6.
        
        Alternative, we can also think of it as (-$2)(+$6)(-$5)(+$7). This means when
        the stock is at $5, we will use our profit to bring its effective price
        down to $1 (i.e. (-$2)(+$6)(-$5)). When we sell at $7, we capture a TOTAL
        profit of $6. Our tabulation is cumulative.
        
                
        If k = 3, we do the same thing:
        
            3, min_price [3, 3, 3], max_profit [0, 0, 0]
            2, min_price [2, 2, 2], max_profit [0, 0, 0]
            6, min_price [2, 2, 2], max_profit [4, 4, 4]
            5, min_price [2, 1, 1], max_profit [4, 4, 4]
            7, min_price [2, 1, 1], max_profit [5, 6, 6]
            0, min_price [0, -5, -6], max_profit [5, 6, 6]
            3, min_price [0, -5, -6], max_profit [5, 8, 9]
        """
        min_price = [float("inf")] * (k + 1)
        max_profit = [0] * (k + 1)
        
        for price in prices:
            for i in range(1, k + 1):
                min_price[i] = min(min_price[i], price - max_profit[i-1])
                max_profit[i] = max(max_profit[i], price - min_price[i])

        return max_profit[k]

if __name__ == "__main__":
    k = 2
    prices = [3,2,6,5,0,3]
    print(Solution().maxProfit(k, prices))
