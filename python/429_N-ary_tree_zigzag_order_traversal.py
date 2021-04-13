# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from python.leetcode_tree_helper import deserialize, TreeNode
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result_list=[]  #Final result list of list is saved here
        if root is None:
            return []

        queue=[]  # each node's children are saved here
        queue.append(root)
        left_right=True

        while(len(queue)>0):  # For each root's child, make it as root and save their left & right child
            current_level_list=[] # Specifically created to save a list of current level elements
            next_level_q=[] # Store children of each node at current level
            for element in queue:
                current_level_list.append(element.val)
                if element.left is not None:
                    next_level_q.append(element.left)
                if element.right is not None:
                    next_level_q.append(element.right)
            if left_right:
                result_list.append(current_level_list)
            else:
                current_level_list.reverse()
                result_list.append(current_level_list)
            left_right= not left_right
            queue=next_level_q  #Updating the queue with next level children to make them current nodes

        return result_list

s=Solution()
root = deserialize('[3,9,20,null,null,15,7]')
print(s.zigzagLevelOrder(root))
