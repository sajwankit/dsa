#
# @lc app=leetcode id=26 lang=python3
# @lcpr version=30203
#
# [26] Remove Duplicates from Sorted Array
#

import sys
import os

from typing import *
from leetcode.nodes import *

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0

        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                nums[slow+1] = nums[fast]
                slow += 1

        return slow+1
# @lc code=end

if __name__ == '__main__':
    solution = Solution()

    # your test code here
    print(solution.removeDuplicates([1,2]))
    print(solution.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))



#
# @lcpr case=start
# [1,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [0,0,1,1,1,2,2,3,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [0,0,1,1,2,3,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end    

# @lcpr case=start
# [1,2]\n
# @lcpr case=end    

# @lcpr case=start
# [1,1]\n
# @lcpr case=end

