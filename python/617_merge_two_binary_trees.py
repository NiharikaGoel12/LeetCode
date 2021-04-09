# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from python.leetcode_tree_helper import deserialize, TreeNode, drawtree


class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        if root1 is None and root2 is None:
            return None
        if root1 is None:
            return root2
        if root2 is None:
            return root1
        sum= root1.val + root2.val
        root = TreeNode(sum)
        root.left= self.mergeTrees(root1.left, root2.left)
        root.right=self.mergeTrees(root1.right, root2.right)

        return root

s=Solution()
root1=deserialize('[1,3,2,5]')
root2=deserialize('[2,1,3,null,4,null,7]')
drawtree(s.mergeTrees(root1, root2))


