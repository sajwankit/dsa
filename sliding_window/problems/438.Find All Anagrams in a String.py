#
# @lc app=leetcode id=438 lang=python3
# @lcpr version=30203
#
# [438] Find All Anagrams in a String
#

import sys
import os

from typing import *
from leetcode.nodes import *

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        l, r = 0, 0
        valid = 0
        window = {}
        pd = {}
        for x in p:
            pd[x] = pd.get(x,0) + 1

        while r < len(s):
            c_put = s[r]

            r += 1 

            if c_put in pd:
                window[c_put] = window.get(c_put, 0) + 1 
                if window[c_put] == pd[c_put]:
                    valid += 1
            
            while (r-l) >= len(p):
                
                if valid == len(pd):
                    ans.append(l)

                c_pop = s[l]

                l += 1

                if c_pop in pd:
                    if window[c_pop] == pd[c_pop]:
                        valid -= 1
                    window[c_pop] = window.get(c_pop, 0) - 1

        return ans
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.findAnagrams("cbaebabacd", "abc"))
    print(s.findAnagrams("abab", "ab"))

#
# @lcpr case=start
# "cbaebabacd"\n"abc"\n
# @lcpr case=end

# @lcpr case=start
# "abab"\n"ab"\n
# @lcpr case=end

#

