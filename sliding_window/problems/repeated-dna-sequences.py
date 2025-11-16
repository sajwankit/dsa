#
# @lc app=leetcode id=187 lang=python3
# @lcpr version=30300
#
# [187] Repeated DNA Sequences
#

import sys
import os

from typing import *
from leetcode.nodes import *

# @lc code=start
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        l, r = 0, 0
        found_substrings = set({})
        window_str = ""
        ans = []
        while r < len(s):

            c = s[r] 

            r += 1 # expand 

            window_str = window_str + c 

            if len(window_str) == 10:

                if window_str in found_substrings and window_str not in ans:
                    ans.append(window_str)
                else:
                    found_substrings.add(window_str)

                c = s[l]

                l += 1 # contract 
                window_str = window_str[1:]
        return ans

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    print(solution.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
    print(solution.findRepeatedDnaSequences("AAAAAAAAAAAAA"))



#
# @lcpr case=start
# "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"\n
# @lcpr case=end

# @lcpr case=start
# "ACGTACGTAAACGTACGTAA"\n
# @lcpr case=end

# @lcpr case=start
# "AAAAAAAAAABAAAAAAAAAAB"\n
# @lcpr case=end


# @lcpr case=start
# "TTTTTTTTTTGGGGGGGGGGTTTTTTTTTT"\n
# @lcpr case=end


# 
# @lcpr case=start
# "AAAAAAAAAAC"\n
# @lcpr case=end

# @lcpr case=start
# "AAAAAAAAAAAAA"\n
# @lcpr case=end

# @lcpr case=start
# "AAGATCGTAAGATCGTA"\n
# @lcpr case=end

# @lcpr case=start
# "ACGTACGTAC"\n
# @lcpr case=end



