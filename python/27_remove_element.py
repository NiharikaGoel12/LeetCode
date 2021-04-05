class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        pointer=0
        nonZero_counter=len(nums)

        while pointer<len(nums):
            if nums[pointer] == val:
                nums[pointer]=0
                nonZero_counter -=1
            pointer += 1

        insertPos=0
        for i in nums:
            if i !=0:
                nums[insertPos] = i
                insertPos +=1

        while insertPos <len(nums):
            nums[insertPos]=0
            insertPos+=1

        return nonZero_counter

s=Solution()
print(s.removeElement(nums = [3,2,2,3], val = 3))

