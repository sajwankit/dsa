#
# @lc app=leetcode id=712 lang=python3
# @lcpr version=30300
#
# [712] Minimum ASCII Delete Sum for Two Strings
#

import sys
import os

from typing import *
from leetcode.nodes import *

# @lc code=start
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        ascii = {chr(i): i for i in range(97, 123)}
        dp = [[None for j in range(len(s2)+1)]  for i in range(len(s1)+1)]

        # s1 -> columns, s2 -> rows 
        # dp[columns][rows]

        dp[0][0] = 0

        for i in range(1, len(s1)+1):
            dp[i][0] = ascii[s1[i-1]] + dp[i-1][0]

        for j in range(1, len(s2)+1):
            dp[0][j] = ascii[s2[j-1]] + dp[0][j-1]


        for j in range(1, len(s2)+1):
            for i in range(1, len(s1)+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    x = ascii[s2[j-1]] + dp[i][j-1]
                    y = ascii[s1[i-1]] + dp[i-1][j]
                    dp[i][j] = min(x, y)
        return dp[-1][-1]

        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    print(solution.minimumDeleteSum("sea", "eat"))
    # your test code here
    print(solution.minimumDeleteSum("delete", "leet"))



#
# @lcpr case=start
# "sea"\n"eat"\n
# @lcpr case=end

# @lcpr case=start
# "delete"\n"leet"\n
# @lcpr case=end

#

