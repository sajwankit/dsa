#
# @lc app=leetcode id=116 lang=python3
# @lcpr version=30304
#
# [116] Populating Next Right Pointers in Each Node
#

import sys
import os

from typing import *
from leetcode.nodes import *

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
Node = TreeNode

from collections import deque
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return root
        
        current_node_depth = 0
        q = deque()
        q.append((root, current_node_depth))

        
        while q:
            current_node, current_node_depth = q.popleft()
            if len(q) != 0:
                if q[0][-1] == current_node_depth:
                    current_node.next = q[0][0]
            lc = current_node.left 
            rc = current_node.right 
            if lc is not None:
                q.append([lc, current_node_depth+1])
            if rc is not None:
                q.append([rc, current_node_depth+1])
        
        return root
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    root = Node.create_root([1,2,3,4,5,6,7])
    result = solution.connect(root)
    # your test code here



#
# @lcpr case=start
# [1,2,3,4,5,6,7]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

# add more test cases here of perfect binary tree 
# @lcpr case=start
# [10,20,30,40,50,60,70,80,90,100,110,120,130,140,150]\n
# @lcpr case=end

