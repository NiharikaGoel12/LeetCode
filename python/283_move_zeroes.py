class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        insertPos=0

        if len(nums)<2:
            return nums

        for each_num in nums:
            if each_num !=0:
                nums[insertPos]= each_num
                insertPos +=1

        while insertPos<len(nums):
            nums[insertPos] =0
            insertPos+=1

        return nums

s=Solution()
print(s.moveZeroes(nums = [0,1,0,3,12]))