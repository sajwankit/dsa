#
# @lc app=leetcode id=139 lang=python3
# @lcpr version=30305
#
# [139] Word Break
#

import sys
import os

from typing import *
from leetcode.nodes import *

# @lc code=start
class Solution:
    
    def __init__(self):
        self.dp = {}
    
    def rec(self, s, wordDict, idx):

        ans = False

        if len(s[idx: ]) == 0:
            return True

        for i in range(idx, len(s)+1):
            if s[idx: i] in wordDict:
                if f"{idx}_{i}" in self.dp:
                    ans = self.dp[f"{idx}_{i}"]
                else:
                    ans = self.rec(s, wordDict, i)
                    self.dp[f"{idx}_{i}"] = ans
                    
                if ans:
                    return True
            else:
                ans = False
                self.dp[f"{idx}_{i}"] = ans
        
        return ans


    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        return self.rec(s, wordDict, 0)
        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # print(solution.wordBreak("aaaaaaa", ["aaaa","aaa"]))
    # print(solution.wordBreak("catsandog", ["cats","dog","sand","and","cat"]))
    print(solution.wordBreak("applepenapple", ["apple","pen"]))
    # your test code here



#
# @lcpr case=start
# "leetcode"\n["leet","code"]\n
# @lcpr case=end

# @lcpr case=start
# "applepenapple"\n["apple","pen"]\n
# @lcpr case=end

# @lcpr case=start
# "catsandog"\n["cats","dog","sand","and","cat"]\n
# @lcpr case=end

#

