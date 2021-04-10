"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from python.leetcode_tree_helper import deserialize
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """


s=Solution()
root=deserialize('[1,null,3,2,4,null,5,6]')
print(s.preorder(root))