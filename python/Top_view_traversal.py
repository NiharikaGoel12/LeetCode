# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from python.leetcode_tree_helper import deserialize, TreeNode
class Solution(object):
    def topSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        level_dict={}
        level_dict[0]=root.val
        queue=[]  # each node's children are saved here
        queue.append((root,0))

        while(len(queue)>0):  # For each root's child, make it as root and save their left & right child
            next_level_q=[] # Store children of each node at current level
            for tup in queue:
                element = tup[0]
                pos = tup[1]
                if pos not in level_dict:
                    level_dict[pos]= element.val
                if element.left is not None:
                    next_level_q.append((element.left, pos - 1))
                if element.right is not None:
                    next_level_q.append((element.right, pos+1))
            queue=next_level_q  #Updating the queue with next level children to make them current nodes
        return list(level_dict.values())

s=Solution()
root = deserialize('[1,2,3,4,5,6,7]')
print(s.topSideView(root))
