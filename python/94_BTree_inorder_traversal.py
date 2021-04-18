# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from python.leetcode_tree_helper import deserialize


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result_list = []
        # self.inOrderRecurs(root,result_list)
        result_list = self.inOrderStack(root)
        return result_list

    def inOrderRecurs(self, root, result_list):
        if root is None:
            return
        self.inOrderRecurs(root.left, result_list)
        result_list.append(root.val)
        self.inOrderRecurs(root.right, result_list)

    def inOrderStack(self, root):
        if root is None:
            return []
        stack = []
        current = root
        result = []

        while stack or current is not None:
            if current:
                stack.append(current)
                current = current.left
            else:
                temp_node = stack.pop()
                result.append(temp_node.val)
                current = temp_node.right
        return result


s=Solution()
root = deserialize('[1,null,2,3]')
print(s.inorderTraversal(root))
