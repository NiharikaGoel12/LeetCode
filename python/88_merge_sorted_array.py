class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        num1_pointer = m-1
        num2_pointer= n-1
        insertPos= len(nums1)-1

        while num1_pointer>=0 and num2_pointer>=0:
            if nums2[num2_pointer] > nums1[num1_pointer]:
                nums1[insertPos] = nums2[num2_pointer]
                num2_pointer -=1
            else:
                nums1[insertPos] = nums1[num1_pointer]
                num1_pointer -=1
            insertPos -=1

        while num2_pointer >=0:
            nums1[insertPos] = nums2[num2_pointer]
            insertPos -=1
            num2_pointer -=1
        return nums1


s=Solution()
print(s.merge(nums1 = [1], m = 1, nums2 = [], n = 0))
