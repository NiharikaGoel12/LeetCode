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
        # self.inOrderTraverse(root,result)
        return self.inOrderStack(root)
        # if len(result)!=len(set(result)):
        #     return False
        # return result==sorted(result)

    def inOrderTraverse(self,root,result):
        if root is None:
            return
        self.inOrderTraverse(root.left,result)
        result.append(root.val)
        self.inOrderTraverse(root.right, result)

    def inOrderStack(self, root):
        if root is None:
            return []
        stack=[]
        prev_el=None
        current=root

        while len(stack)>0 or current is not None:
            if current is not None:
                stack.append(current)
                current=current.left
            else:
                temp_node=stack.pop()
                current=temp_node.right
                if prev_el and temp_node.val<prev_el:
                    return False
                prev_el=temp_node.val
        return True

s=Solution()
root = deserialize('2,1,3]')
print(s.isValidBST(root))
