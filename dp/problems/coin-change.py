#
# @lc app=leetcode id=322 lang=python3
# @lcpr version=30203
#
# [322] Coin Change
#

import sys
import os

from typing import *
from leetcode.nodes import *

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount+1)
        dp[0] = 0 

        for sub_amount in range(1, amount+1):
            for coin in coins:
                if sub_amount-coin >= 0:
                    dp[sub_amount] = min(dp[sub_amount], dp[sub_amount-coin] + 1) 

        return dp[-1] if dp[-1] != float('inf') else -1
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    solution.coinChange([1,2,5], 11)
    # your test code here



#
# @lcpr case=start
# [1,2,5]\n11\n
# @lcpr case=end
