# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from python.leetcode_tree_helper import deserialize, TreeNode
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result_map={}
        level=0
        self.rightViewTrans(root, level, result_map)
        return result_map.values()

    def rightViewTrans(self, root, level, result_map):
        if root is None:
            return
        if level not in result_map:
            result_map[level]=root.val

        self.rightViewTrans(root.right, level+1, result_map)
        self.rightViewTrans(root.left, level + 1, result_map)



s=Solution()
root = deserialize('[1,2,3,null,5,null,4]')
print(s.rightSideView(root))
