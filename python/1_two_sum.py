class Solution(object):
    def twoSum(self, arr1, s):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        difference_dict={}

        for index in range(0, len(arr1)):
            num=arr1[index]
            if num in difference_dict:
                return [difference_dict[num], index]
            else:
                difference_dict[s-num]=index
        return []

s=Solution()
print(s.twoSum(arr1=[3,3], s=6))
