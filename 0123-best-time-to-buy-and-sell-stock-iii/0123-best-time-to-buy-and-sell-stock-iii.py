class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        dp = [[[-1]*2 for _ in range(3)] for _ in range(n)]
        def f(i, buy, k):
            if i==n:
                return 0
            if k==0:
                return 0
            if dp[i][k][buy]!=-1:
                return dp[i][k][buy]
            ans = 0
            ans = f(i+1, buy, k)
            if buy==0:
                ans = max(ans, -prices[i]+f(i+1, 1, k))
            else:
                ans = max(ans, prices[i]+f(i+1, 0, k-1))
            dp[i][k][buy] = ans
            return dp[i][k][buy]
        return f(0,0,2)