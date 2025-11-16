#
# @lc app=leetcode id=424 lang=python3
# @lcpr version=30304
#
# [424] Longest Repeating Character Replacement
#

import sys
import os

from typing import *
from leetcode.nodes import *

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0

        window = dict({})

        ans = 0

        def get_max_count_char(window):
            max_count = -float('inf')
            for c in window.keys():
                max_count = max(max_count, window[c])
            return max_count


        while r < len(s):

            ins = s[r] 

            r += 1 

            window[ins] = window.get(ins, 0) + 1 

            # update maxcount char 
            max_count = get_max_count_char(window) 

            if (r-l) - max_count <= k:
                ans = max(ans, (r-l))


            while ( (r-l) - max_count > k ):

                popc = s[l] 

                l += 1 

                window[popc] = window[popc] - 1 

                max_count = get_max_count_char(window) 

                if (r-l) - max_count <= k:
                    ans = max(ans, (r-l))

        return ans
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    print(solution.characterReplacement("AABABBA", 1))
    print(solution.characterReplacement("ABAB", 2))
    
    # your test code here

    # Edge and tricky cases
    print(solution.characterReplacement("", 2))                # Empty string, expect 0
    print(solution.characterReplacement("A", 0))               # Single character, expect 1
    print(solution.characterReplacement("AAAA", 2))            # All same, expect 4
    print(solution.characterReplacement("ABCDE", 1))           # All different, k=1, expect 2
    print(solution.characterReplacement("ABCDE", 4))           # All different, k=4, expect 5
    print(solution.characterReplacement("AABACCA", 2))         # Multiple possible windows, expect 5
    print(solution.characterReplacement("ABBB", 2))            # Replace A to B, expect 4
    print(solution.characterReplacement("BAAAAB", 2))          # Replace B's to A, expect 6
    print(solution.characterReplacement("ABABBAAABBB", 3))     # Mixed, expect 8



#
# @lcpr case=start
# "ABAB"\n2\n
# @lcpr case=end

# @lcpr case=start
# "AABABBA"\n1\n
# @lcpr case=end

#

