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
        result_list=[]  #Final result list of list is saved here
        if root is None:
            return []

        queue=[]  # each node's children are saved here
        queue.append(root)

        while(len(queue)>0):  # For each root's child, make it as root and save their left & right child
            next_level_q=[] # Store children of each node at current level
            for element in queue:
                if element.right is not None:
                    next_level_q.append(element.right)
                if element.left is not None:
                    next_level_q.append(element.left)
            result_list.append(queue[0].val)
            queue=next_level_q  #Updating the queue with next level children to make them current nodes

        return result_list

s=Solution()
root = deserialize('[3,9,20,null,null,15,7]')
print(s.rightSideView(root))
