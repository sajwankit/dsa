#
# @lc app=leetcode id=1011 lang=python3
# @lcpr version=30304
#
# [1011] Capacity To Ship Packages Within D Days
#

import sys
import os

from typing import *
from leetcode.nodes import *

# @lc code=start
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def x(ship_capacity):

            # bad logic :(  could be simplified, but works
            req_days = 0

            curr_total_weight = 0

            for w in weights:
                if curr_total_weight + w < ship_capacity:
                    curr_total_weight += w
                elif curr_total_weight + w == ship_capacity:
                    req_days += 1
                    curr_total_weight = 0
                elif curr_total_weight + w > ship_capacity:
                    req_days += 1
                    curr_total_weight = w
            if curr_total_weight > 0:
                req_days += 1
            return req_days 

        l = max(weights)
        r = sum(weights)

        while l <= r:

            ship_capacity = l + (r-l)//2 

            req_days = x(ship_capacity)

            if req_days < days:
                r = ship_capacity - 1
            
            elif req_days > days:
                l = ship_capacity + 1
            
            elif req_days == days:
                r = ship_capacity - 1

        return l
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    print(solution.shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5))
    print(solution.shipWithinDays([3,2,2,4,1,4], 3))
    print(solution.shipWithinDays([1,2,3,1,1], 4))
    print(solution.shipWithinDays([10,50,100,100,50,100,100], 5)) # expected 160
    print(solution.shipWithinDays([1,2,3,4,5,6,7,8,9,10], 1)) # expected 55
    print(solution.shipWithinDays([1,2,3,4,5,6,7,8,9,10], 10)) # expected 10
    # your test code here



#
# @lcpr case=start
# [1,2,3,4,5,6,7,8,9,10]\n5\n
# @lcpr case=end

# @lcpr case=start
# [3,2,2,4,1,4]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,1,1]\n4\n
# @lcpr case=end

#

