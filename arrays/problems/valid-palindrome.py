#
# @lc app=leetcode id=125 lang=python3
# @lcpr version=30203
#
# [125] Valid Palindrome
#

import sys
import os

from typing import *
from leetcode.nodes import *

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = "".join([x.lower() for x in s if x.isalnum()])

        a=0
        z=len(s)-1

        ans = True
        while a<z:
            if s[a] != s[z]:
                ans = False 
                break 
            a+=1
            z-=1

        return ans
                
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    print(solution.isPalindrome("0P"))
    print(solution.isPalindrome("race a car"))
    print(solution.isPalindrome(" "))


#
# @lcpr case=start
# "0P"\n
# @lcpr case=end

# @lcpr case=start
# "race a car"\n
# @lcpr case=end

# @lcpr case=start
# " "\n
# @lcpr case=end

#

