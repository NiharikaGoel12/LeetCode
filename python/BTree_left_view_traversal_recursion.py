# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from python.leetcode_tree_helper import deserialize, TreeNode
class Solution(object):
    def leftSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result_dict={}
        level=0
        self.leftViewTrans(root,level, result_dict)
        return result_dict.values()


    def leftViewTrans(self,root,level,result_dict):
        if root is None:
            return
        if level not in result_dict:
            result_dict[level]=root.val

        self.leftViewTrans(root.left, level+1, result_dict)
        self.leftViewTrans(root.right, level + 1, result_dict)

s=Solution()
root = deserialize('[1,2,3,null,5,null,4]')
print(s.leftSideView(root))
