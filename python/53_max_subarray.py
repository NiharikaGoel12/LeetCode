class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = max(nums)
        running_sum=0

        for i in range(0, len(nums)):
            if nums[i] + running_sum < 0:
                running_sum =0
            else:
                running_sum += nums[i]
                max_sum = max(max_sum, running_sum)

        return max_sum

s=Solution()
print(s.maxSubArray(nums = [-5,-4,-1,-7,-8]))
