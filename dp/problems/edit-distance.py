#
# @lc app=leetcode id=72 lang=python3
# @lcpr version=30203
#
# [72] Edit Distance
#

import sys
import os

from typing import *
from leetcode.nodes import *

# @lc code=start
class Solution:
    def minDistance_tab(self, word1: str, word2: str) -> int:
        dp = [[0] * (len(word2)+1) for i in range(len(word1)+1)]
        for i in range(1, len(word1)+1):
            dp[i][0] = i

        for j in range(1, len(word2)+1):
            dp[0][j] = j

        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if (i==0) or (j==0):
                    continue 
                # exact match 
                if word1[i-1] == word2[j-1]: # -1 because when i=5, character should be word[4]
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # insert 
                    x1 = 1 + dp[i][j-1]
                    # delete 
                    x2 = 1 + dp[i-1][j]
                    # replace 
                    x3 = 1 + dp[i-1][j-1]
                    dp[i][j] = min(x1, x2, x3)

        return dp[len(word1)][len(word2)]
    
    def minDistance(self, word1: str, word2: str) -> int:
        """
        Space complexity O(n) where n is length of word2
        Time complexity O(m*n) where m is length of word1 and n is length of
        """
        
        if not len(word1):
            return len(word2)
        if not len(word2):
            return len(word1)

        ans = [x for x in range(1,len(word2)+1)]
        for i in range(1, len(word1)+1):
            d, t = i-1, i
            for j in range(1, len(word2)+1):
                l = ans[j-1]
                if word1[i-1] == word2[j-1]:
                    ans[j-1] = d
                else:
                    ans[j-1] = min(d, t, l) + 1
                d = l
                t = ans[j-1]
        return ans[-1] if ans else 0
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    print(solution.minDistance("b", ""))
    # your test code here

# @lcpr case=start
# "aaaa"\n""\n
# @lcpr case=end

#
# @lcpr case=start
# "horse"\n"ros"\n
# @lcpr case=end

# @lcpr case=start
# "intention"\n"execution"\n
# @lcpr case=end

#

