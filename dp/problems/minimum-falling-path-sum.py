#
# @lc app=leetcode id=931 lang=python3
# @lcpr version=30300
#
# [931] Minimum Falling Path Sum
#

import sys
import os

from typing import *
from leetcode.nodes import *

# @lc code=start
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        dp = [[float('inf')] * len(matrix[0]) for _ in range(len(matrix))]
        n_rows = len(matrix)
        n_cols = len(matrix[0])

        # base case, last row, i = n_rows-1 
        for j in range(n_cols):
            dp[n_rows-1][j] = matrix[n_rows-1][j]


        for i in range(n_rows-2, -1, -1):
            for j in range(n_cols):

                # choice you can make 
                #select below 
                p1 = dp[i+1][j]
                p2 = dp[i+1][j-1] if j-1 >= 0 else float('inf')
                p3 = dp[i+1][j+1] if j+1 <= n_cols-1 else float('inf')
                dp[i][j] = matrix[i][j] + min(p1, p2, p3)

        return min(dp[0])
        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    print(solution.minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]]))
    # your test code here
    print(solution.minFallingPathSum([[-19,57],[-40,-5]]))



#
# @lcpr case=start
# [[2,1,3],[6,5,4],[7,8,9]]\n
# @lcpr case=end

# @lcpr case=start
# [[-19,57],[-40,-5]]\n
# @lcpr case=end

#

