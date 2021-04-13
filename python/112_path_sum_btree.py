# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from python.leetcode_tree_helper import deserialize, TreeNode, drawtree
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if root is None:
            return False

        if root.left is None and root.right is None and root.val==targetSum:
            return True

        targetSum -=root.val

        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)

s=Solution()
root = deserialize('[5,4,8,11,null,13,4,7,2,null,null,null,1]')
# drawtree(root)
print(s.hasPathSum(root, targetSum = 22))
