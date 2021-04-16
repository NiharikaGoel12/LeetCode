# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from python.leetcode_tree_helper import deserialize
class Solution(object):
    def isValidBST(self, root):
        result=[]
        self.inOrderTraverse(root,result)
        if len(result)!=len(set(result)):
            return False
        return result==sorted(result)

    def inOrderTraverse(self,root,result):
        if root is None:
            return
        self.inOrderTraverse(root.left,result)
        result.append(root.val)
        self.inOrderTraverse(root.right, result)

s=Solution()
root = deserialize('2,1,3]')
print(s.isValidBST(root))
