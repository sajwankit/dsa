#
# @lc app=leetcode id=226 lang=python3
# @lcpr version=30304
#
# [226] Invert Binary Tree
#

import sys
import os

from typing import *
from leetcode.nodes import *

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return
        x = root.left
        root.left = root.right 
        root.right = x 
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    print()
    # your test code here



#
# @lcpr case=start
# [4,2,7,1,3,6,9]\n
# @lcpr case=end

# @lcpr case=start
# [2,1,3]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#

