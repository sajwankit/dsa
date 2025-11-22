#
# @lc app=leetcode id=875 lang=python3
# @lcpr version=30304
#
# [875] Koko Eating Bananas
#

import sys
import os

from typing import *
from leetcode.nodes import *

# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        piles = sorted(piles)

        kmin, kmax = 0, piles[-1]

        def get_hours(k):
            hr_list = [math.ceil(x/k) for x in piles]
            return sum(hr_list)

        # binary search over kmin, kmax range to find optimum k 

        # k_list = list(range(kmin, kmax+1))

        l, r = 1, kmax


        while l <= r:

            mid = l + (r-l)//2 

            k_hrs = get_hours(mid)

            if k_hrs < h:
                r = mid -1 
            
            if k_hrs > h:
                l = mid + 1 
            
            if k_hrs == h:
                r = mid - 1

        return l

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    print(solution.minEatingSpeed([3,6,7,11], 8))
    print(solution.minEatingSpeed([30,11,23,4,20], 5))
    print(solution.minEatingSpeed([30,11,23,4,20], 6))
    print(solution.minEatingSpeed([312884470], 312884469))
    print(solution.minEatingSpeed([312884470], 968709470))
    # your test code here



#
# @lcpr case=start
# [3,6,7,11]\n8\n
# @lcpr case=end

# @lcpr case=start
# [30,11,23,4,20]\n5\n
# @lcpr case=end

# @lcpr case=start
# [30,11,23,4,20]\n6\n
# @lcpr case=end

#

