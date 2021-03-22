from collections import Counter
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_dict= Counter(nums)

        for key,value in nums_dict.items():
            if value >=2:
                return True

        return False


s=Solution()
print(s.containsDuplicate(nums = [1,1,1,3,3,4,3,2,4,2]))
