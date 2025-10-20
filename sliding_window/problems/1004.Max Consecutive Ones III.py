#
# @lc app=leetcode id=1004 lang=python3
# @lcpr version=30203
#
# [1004] Max Consecutive Ones III
#
import sys
import os

from typing import *
from leetcode.nodes import *
# @lc code=start
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, r = 0, 0
        c = 0
        ans = 0

        while r < len(nums):

            include_ele = nums[r]

            r += 1 

            if include_ele == 0:
                c += 1 

            while c > k and l <= r and l < len(nums):
                
                if nums[l] == 0:
                    c -= 1

                l += 1

            if c <= k:
                ans = max(ans, (r-l))

        return ans
        
# @lc code=end

if __name__ == "__main__":
    s = Solution()
    # print(s.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))
    print(s.longestOnes([0, 0,1,1,0,0, 1,1,1,0,1,1,0,0,0,1,1,1,1], 3))

#
# @lcpr case=start
# [1,1,1,0,0,0,1,1,1,1,0]\n2\n
# @lcpr case=end

# @lcpr case=start
# [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]\n3\n
# @lcpr case=end

#

