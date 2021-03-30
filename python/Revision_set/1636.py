from collections import Counter
class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        nums_dict= Counter(nums)
        ''' In case key value is same, take decreasing order via '-key'''
        size = lambda key:(nums_dict[key], -key)
        nums.sort(key= size)
        return nums



s=Solution()
print(s.frequencySort(nums = [2,3,1,3,2]))
print(s.frequencySort(nums = [1,1,2,2,2,3]))
print(s.frequencySort(nums = [-1,1,-6,4,5,-6,1,4,1]))