# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from python.leetcode_tree_helper import deserialize
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if root is None:
            return None
        stack=[]
        counter=1
        current=root

        while len(stack)>0 or current is not None:
            if current is not None:
                stack.append(current)
                current=current.left
            else:
                temp_node=stack.pop()
                current=temp_node.right
                if counter==k:
                    return temp_node.val
                counter+=1
        return None

s=Solution()
root = deserialize('[3,1,4,null,2]')
print(s.kthSmallest(root,k=1))
