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
        result_list=[]
        queue=[]

        if root is None:
            return []
        queue.append(root)

        while len(queue)>0:
            child_q=[]
            for child in queue:
                if child.left is not None:
                    child_q.append(child.left)
                if child.right is not None:
                    child_q.append(child.right)
            result_list.append(queue[0])
            queue=child_q

        return result_list

s=Solution()
root = deserialize('[1,2,3,null,5,null,4]')
print(s.leftSideView(root))
