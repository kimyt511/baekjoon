# 279 Perfect Squares

import math


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [-1] * (n + 1)

        def getVal(n):
            if dp[n] != -1:
                return dp[n]
            if math.sqrt(n) % 1 == 0:
                return 1
            val = 10000
            for i in range(1, math.ceil(math.sqrt(n)) + 1):
                if i * i <= n:
                    val = min(val, getVal(n - i * i) + 1)
            dp[n] = val
            return val

        return getVal(n)
