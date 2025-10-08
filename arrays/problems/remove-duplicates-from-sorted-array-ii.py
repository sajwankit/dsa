#
# @lc app=leetcode id=80 lang=python3
# @lcpr version=30203
#
# [80] Remove Duplicates from Sorted Array II
#

import sys
import os

from typing import *
from leetcode.nodes import *

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s=0
        full_flag=False 

        for f in range(1, len(nums)):
            if nums[f] == nums[s]:
                if not full_flag:
                    nums[s+1] = nums[f]
                    full_flag = True 
                    s += 1
            elif nums[f] != nums[s]:
                nums[s+1] = nums[f]
                s += 1 
                full_flag = False
        return s+1
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    nums = [0, 1,1,1,1,1,1,2,2,2,3,3,3,3,4,5,5,6]
    print(solution.removeDuplicates(nums))
    # your test code here




#
# @lcpr case=start
# [1,1,1,2,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [0,0,1,1,1,1,2,3,3]\n
# @lcpr case=end

#

