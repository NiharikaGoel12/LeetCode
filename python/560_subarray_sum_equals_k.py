from collections import defaultdict
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        cont_dict=defaultdict(int)
        cont_dict[0]=1
        running_sum=0
        result = 0

        for each_num in nums:
            running_sum +=each_num
            if (running_sum-k) in cont_dict:
                result = result + cont_dict[running_sum -k]
            cont_dict[running_sum]= cont_dict[running_sum]+ 1

        return result

s=Solution()
print(s.subarraySum(nums = [1,2,3], k = 3))







