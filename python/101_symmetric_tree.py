# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from python.leetcode_tree_helper import deserialize
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        return self.checkSymmetry(root.left, root.right)

    def checkSymmetry(self, p, q):

        if p is None or q is None:
            if p is None and q is None:
                return True
            else:
                return False

        if p.val != q.val:
            return False
        return self.checkSymmetry(p.left, q.right) and self.checkSymmetry(p.right, q.left)


s = Solution()
root = deserialize('[1,2,2,null,3,null,3]')
print(s.isSymmetric(root))



