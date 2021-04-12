"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        result_list=[]  #Final result list of list is saved here
        if root is None:
            return []

        queue=[]  # each node's children are saved here
        queue.append(root)

        while len(queue)>0:  # For each root's child, make it as root and save their left & right child
            current_level_list=[] # Specifically created to save a list of current level elements
            next_level_q=[] # Store children of each node at current level
            for element in queue:
                current_level_list.append(element.val)
                for child in element.children:
                    next_level_q.append(child)
            result_list.append(current_level_list)
            queue=next_level_q  #Updating the queue with next level children to make them current nodes

        return result_list
