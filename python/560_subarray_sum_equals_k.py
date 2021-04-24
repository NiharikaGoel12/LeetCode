class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # count_occur=0
        # p1=0
        #
        # while p1<len(nums):
        #     if nums[p1]==k:
        #         count_occur+=1
        #     running_sum = nums[p1]
        #     for j in range(p1+1, len(nums)):
        #         if running_sum+nums[j]==k:
        #             count_occur+=1
        #         running_sum+=nums[j]
        #     p1+=1
        #
        # return count_occur

        running_sum=0
        running_list=[0]
        for i in range(0,len(nums)):
            running_sum +=nums[i]
            running_list.append(running_sum)

s=Solution()
print(s.subarraySum(nums = [1,3,-3,1,2,3,-3,1], k = 3))





