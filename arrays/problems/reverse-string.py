#
# @lc app=leetcode id=344 lang=python3
# @lcpr version=30203
#
# [344] Reverse String
#

import sys
import os

from typing import *
from leetcode.nodes import *

# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        a = 0
        b = len(s)-1 

        while a < b:
            t = s[a]
            s[a] = s[b]
            s[b] = t 
            a += 1
            b -= 1
        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here



#
# @lcpr case=start
# ["h","e","l","l","o"]\n
# @lcpr case=end

# @lcpr case=start
# ["H","a","n","n","a","h"]\n
# @lcpr case=end

#

