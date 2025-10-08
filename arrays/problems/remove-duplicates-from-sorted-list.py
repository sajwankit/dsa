#
# @lc app=leetcode id=83 lang=python3
# @lcpr version=30203
#
# [83] Remove Duplicates from Sorted List
#

import sys
import os

from typing import *
from leetcode.nodes import *

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None: return head
        s = head
        f = head.next
        while True:
            if s.val != f.val:
                s.next = f 
                s = f
            if f.next is None:  break
            f = f.next
        s.next = None
        return head
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    
    # define a linked list for testing
    head = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
    result = solution.deleteDuplicates(head)
    while result:
        print(result.val, end=" -> ")
        result = result.next
    print("None")
    # your test code here



#
# @lcpr case=start
# [1,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,2,3,3]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

