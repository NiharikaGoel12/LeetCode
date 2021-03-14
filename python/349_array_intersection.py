class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        unique_num1 = list(set(nums1))
        unique_num2 = list(set(nums2))

        common_num=[]

        for i in unique_num1:
            for j in unique_num2:
                if i==j:
                    common_num.append(i)

        return common_num

s = Solution()
print(s.intersection(nums1=[4,9,5], nums2=[9,4,9,8,4]))