# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from python.leetcode_tree_helper import TreeNode
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.arraytoBST(nums,0,len(nums)-1)

    def arraytoBST(self,nums,low,high):
        if len(nums)==0:
            return None
        mid=int((low+high)/2)

        root=TreeNode(nums[mid])
        root.left=self.arraytoBST(nums, low, mid-1)
        root.right = self.arraytoBST(nums, mid+1, high)

        return root

s=Solution()
print(s.sortedArrayToBST(nums = [-10,-3,0,5,9]))
