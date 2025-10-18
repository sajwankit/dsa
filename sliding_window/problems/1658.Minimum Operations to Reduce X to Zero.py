#
# @lc app=leetcode id=1658 lang=python3
# @lcpr version=30203
#
# [1658] Minimum Operations to Reduce X to Zero
#
import sys
import os

from typing import *
from leetcode.nodes import *
# @lc code=start
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        if len(nums) == 1:
            return 1 if nums[0] == x else -1

        l, r = 0, 0 # empty window 
        s = sum(nums)
        req_window_sum = s - x 

        curr_window_sum = 0
        ans = float('inf')
        while r < len(nums):
            include_n = nums[r] 

            r += 1 # expand the window 

            curr_window_sum += include_n # update the window sum 

            while (curr_window_sum >= req_window_sum) and l<=r and l<len(nums):

                if curr_window_sum == req_window_sum:
                    ans = min(ans, len(nums) - (r-l))

                exclude_n = nums[l]

                l += 1 # shrink the window 

                curr_window_sum -= exclude_n 
            
        return ans if ans != float('inf') else -1
    

if __name__ == "__main__":
    s = Solution()
    print(s.minOperations([5], 5))
    print(s.minOperations([1,1], 3))
    print(s.minOperations([5,2,3,1,1], 5))
    print(s.minOperations([5,6,7,8,9], 4))
    print(s.minOperations([3,2,20,1,1,3], 10))

# @lc code=end


# @lcpr case=start
# [5,2,3,1,1]\n5\n
# @lcpr case=end


#
# @lcpr case=start
# [1,1,4,2,3]\n5\n
# @lcpr case=end

# @lcpr case=start
# [5,6,7,8,9]\n4\n
# @lcpr case=end

# @lcpr case=start
# [3,2,20,1,1,3]\n10\n
# @lcpr case=end

#

