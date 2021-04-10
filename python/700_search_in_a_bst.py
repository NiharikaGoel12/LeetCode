# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from python.leetcode_tree_helper import deserialize
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root is None:
            return []
        if root.val<val:
            self.searchBST(root.right, val)
        if root.val>val:
            self.searchBST(root.left, val)



s=Solution()
root=deserialize('[4,2,7,1,3]')
print(s.searchBST(root, val=2))