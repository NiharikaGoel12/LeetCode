# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from python.leetcode_tree_helper import deserialize
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        if root is None:
            return 0
        sum=0
        if root.val>=low and root.val<=high:
            sum +=root.val

        if root.val<high:
            sum += self.rangeSumBST(root.right, low, high)

        if root.val >low:
            sum += self.rangeSumBST(root.left, low, high)

        return sum

s=Solution()
root = deserialize('[10,5,15,3,7,null,18]')
print(s.rangeSumBST(root, low=7, high=15))
