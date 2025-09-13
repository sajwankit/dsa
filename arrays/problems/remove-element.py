#
# @lc app=leetcode id=27 lang=python3
# @lcpr version=30203
#
# [27] Remove Element
#

import sys
import os

from typing import *
from leetcode.nodes import *

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        s=0
        f=0
        for f in range(len(nums)):
            if nums[f] != val:
                nums[s] = nums[f] 
                s += 1 
        return s
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here



#
# @lcpr case=start
# [3,2,2,3]\n3\n
# @lcpr case=end

# @lcpr case=start
# [0,1,2,2,3,0,4,2]\n2\n
# @lcpr case=end

#

