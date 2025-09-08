#
# @lc app=leetcode id=300 lang=python3
# @lcpr version=30202
#
# [300] Longest Increasing Subsequence
#

import sys
import os

from typing import *
from leetcode.nodes import *

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp) if dp else 0
    
# @lc code=end

# at each index, store the lis possible which includes the num at that index
if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLIS([1, 5, 2, 4]))
    # your test code here



#
# @lcpr case=start
# [10,9,2,5,3,7,101,18]\n
# @lcpr case=end