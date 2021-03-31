class Solution(object):
    def maxAscendingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        running_sum = nums[0]
        result=0

        if len(nums) ==1:
                return nums[0]
        else:
            for i in range(1, len(nums)):
                if nums[i] > nums[i-1]:
                    running_sum += nums[i]
                else:
                    running_sum = nums[i]
                result = max(result, running_sum)
            return result

s=Solution()
print(s.maxAscendingSum(nums = [5,5,6,6,6,9,1,2]))