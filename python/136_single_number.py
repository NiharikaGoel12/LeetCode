class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_dict= {}
        for i in nums:
            if i in nums_dict:
                nums_dict[i] +=1
            else:
                nums_dict[i] = 1

        for key, value in nums_dict.items():
            if value ==1:
                return key

s = Solution()
print(s.singleNumber(nums=[4,1,2,1,2]))
