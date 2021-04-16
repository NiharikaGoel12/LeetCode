# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from python.leetcode_tree_helper import deserialize
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            root.left, root.right=self.invertTree(root.right), self.invertTree(root.left)
        return root

s=Solution()
root = deserialize('[4,2,7,1,3,6,9]')
print(s.invertTree(root))
