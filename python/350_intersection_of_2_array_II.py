from collections import Counter
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1_dict= Counter(nums1)
        nums2_dict=Counter(nums2)
        common_elements=[]

        for key,value in nums1_dict.items():
            if key in nums2_dict:
                common_elements.extend([key] * min(nums1_dict[key], nums2_dict[key]))

        return common_elements

s=Solution()
print(s.intersect(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))
