# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from python.leetcode_tree_helper import deserialize, TreeNode, drawtree
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        # print("calculating height of {}".format(root.val))
        result = 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        # print("height of {} is {}".format(root.val, result))
        return result

s=Solution()
root=deserialize('[3,9,20,null,null,15,7]')
print(s.maxDepth(root))