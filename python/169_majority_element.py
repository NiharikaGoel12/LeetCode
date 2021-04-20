from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_dict=Counter(nums)
        return max(nums_dict, key=lambda key:nums_dict[key])
        # return max(nums_dict.items(), key=operator.itemgetter(1))[0]

s=Solution()
print(s.majorityElement(nums = [3,2,3]))
