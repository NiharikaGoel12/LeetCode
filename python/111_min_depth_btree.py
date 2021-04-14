# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from python.leetcode_tree_helper import deserialize, TreeNode
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        leftNode=self.minDepth(root.left)
        rightNode=self.minDepth(root.right)

        if root.left is None and root.right is not None:
            return 1+rightNode

        if root.right is None and root.left is not None:
            return 1+leftNode

        return 1+min(leftNode, rightNode)

s=Solution()
root = deserialize('[2,null,3,null,4,null,5,null,6]')
print(s.minDepth(root))
