#
# @lc app=leetcode id=167 lang=python3
# @lcpr version=30203
#
# [167] Two Sum II - Input Array Is Sorted
#

import sys
import os

from typing import *
from leetcode.nodes import *

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s = 0
        f = len(numbers)-1

        while s<f:
            if numbers[s] + numbers[f] == target:
                return [s+1, f+1]
            elif numbers[s] + numbers[f] > target:
                # we cannot increase s because that will make the sum even bigger
                # we can only decrease the f, that will make the sum closer to target in this case
                f -= 1
            elif numbers[s] + numbers[f] < target:
                # we cannot decrease f, because that will make the sum even smaller, further away from target 
                # we can increase s to make the sum closer to target in this case
                s += 1
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here



#
# @lcpr case=start
# [2,7,11,15]\n9\n
# @lcpr case=end

# @lcpr case=start
# [2,3,4]\n6\n
# @lcpr case=end

# @lcpr case=start
# [-1,0]\n-1\n
# @lcpr case=end

#

